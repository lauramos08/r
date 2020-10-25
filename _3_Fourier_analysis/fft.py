import cv2
import numpy as np
import os
import sys

""" Compute and visualize fft of an image

    python fft.py <path_to_image> <image_name>
"""

if __name__ == '__main__':
    path = sys.argv[1]
    image_name = sys.argv[2]
    path_file = os.path.join(path, image_name)

    # Read the image
    image = cv2.imread(path_file)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_gray_fft = np.fft.fft2(image_gray)
    image_gray_fft_shift = np.fft.fftshift(image_gray_fft)

    # fft visualization
    image_gray_fft_mag = np.absolute(image_gray_fft_shift)
    image_fft_view = np.log(image_gray_fft_mag + 1)
    image_fft_view = image_fft_view / np.max(image_fft_view)

    # sinusoid generation
    num_rows, num_cols = (512, 512)
    enum_rows = np.linspace(0, num_rows - 1, num_rows)
    enum_cols = np.linspace(0, num_cols - 1, num_cols)
    col_iter, row_iter = np.meshgrid(enum_cols, enum_rows)
    u, v = (4, 20)
    sinusoid_image = np.sin(2 * np.pi * (u * row_iter / num_rows + v * col_iter / num_cols))

    # sinusoid visualization
    sinusoid_image = np.sin(2 * np.pi * (u * row_iter / num_rows + v * col_iter / num_cols))
    sinusoid_image_view = (sinusoid_image + 1) / 2
    sinusoid_image_view = (255 * sinusoid_image_view).astype(np.uint8)

    image_gray_fft = np.fft.fft2(sinusoid_image)
    image_gray_fft_shift = np.fft.fftshift(image_gray_fft)

    # fft visualization
    image_gray_fft_mag = np.absolute(image_gray_fft_shift)
    image_fft_view = np.log(image_gray_fft_mag + 1)
    image_fft_view = image_fft_view / np.max(image_fft_view)

    cv2.imshow("Image", sinusoid_image_view)
    cv2.waitKey(0)
