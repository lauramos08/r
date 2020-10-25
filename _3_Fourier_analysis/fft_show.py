import cv2
import numpy as np

""" FFT class to properly visualize fft of gray image

"""


class FFT:
    def __init__(self, image, n):
        shape = image.shape
        if image.ndim == 3:
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            image_gray = image
        image_with_zeros = np.zeros((max(n, shape[0]), max(n, shape[1])), dtype=np.float)
        image_with_zeros[0:shape[0], 0:shape[1]] = np.copy(image_gray)
        self.image_gray = image_with_zeros

    def display(self):
        image_gray_fft = np.fft.fft2(self.image_gray)
        image_gray_fft_shift = np.fft.fftshift(image_gray_fft)

        image_gray_fft_mag = np.absolute(image_gray_fft_shift)
        image_fft_view = np.log(image_gray_fft_mag + 1)
        image_fft_view = image_fft_view / np.max(image_fft_view)
        cv2.imshow("FFT", image_fft_view)
        cv2.waitKey(0)
