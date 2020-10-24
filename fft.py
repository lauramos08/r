import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

if __name__ == '__main__':
    # path = '/Users/julian.quiroga/Downloads/imagenes_vision_puj/imagenes'
    # image_name = 'lena.png'
    # path_file = os.path.join(path, image_name)
    # image = cv2.imread(path_file)
    # image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # image_gray_fft = np.fft.fft2(image_gray)
    # image_gray_fft_shift = np.fft.fftshift(image_gray_fft)
    #
    # # fft visualization
    # image_gray_fft_mag = np.absolute(image_gray_fft_shift)
    # image_fft_view = np.log(image_gray_fft_mag + np.finfo(np.float32).eps)
    # image_fft_view = image_fft_view / np.max(image_fft_view)

    # sinusoid generation
    num_rows, num_cols = (512, 512)
    enum_rows = np.linspace(0, num_rows - 1, num_rows)
    enum_cols = np.linspace(0, num_cols - 1, num_cols)
    col_iter, row_iter = np.meshgrid(enum_cols, enum_rows)
    u, v = (4, 20)
    # omega = np.sqrt(u**2 + v**2)

    # sinusoid visualization
    sinusoid_image = np.sin(2 * np.pi * (u * row_iter / num_rows + v * col_iter / num_cols))
    sinusoid_image += np.sin(2 * np.pi * (v * row_iter / num_rows + u * col_iter / num_cols))
    sinusoid_image_view = (sinusoid_image + 1) / 2
    sinusoid_image_view = (255 * sinusoid_image_view).astype(np.uint8)

    image_gray_fft = np.fft.fft2(sinusoid_image)
    image_gray_fft_shift = np.fft.fftshift(image_gray_fft)

    # fft visualization
    image_gray_fft_mag = np.absolute(image_gray_fft_shift)
    image_fft_view = np.log(1 + image_gray_fft_mag)
    image_fft_view = image_fft_view / np.max(image_fft_view)

    # # ideal filter
    # num_rows, num_cols = (image_gray.shape[0], image_gray.shape[1])
    # enum_rows = np.linspace(0, num_rows - 1, num_rows)
    # enum_cols = np.linspace(0, num_cols - 1, num_cols)
    # col_iter, row_iter = np.meshgrid(enum_cols, enum_rows)
    # low_pass = np.zeros_like(image_gray)
    # high_pass = np.zeros_like(image_gray)
    # radius = int(num_cols / 8)
    # idx = np.sqrt((col_iter - num_cols / 2) ** 2 +
    #               (row_iter - num_rows / 2) ** 2) < radius
    # low_pass[idx] = 1
    # high_pass = 1 - low_pass
    # fft_filtered = image_gray_fft_shift * high_pass
    # image_filtered = np.fft.ifft2(np.fft.fftshift(fft_filtered))
    # image_filtered = np.absolute(image_filtered)

    cv2.imshow("Image", sinusoid_image_view)
    cv2.waitKey(0)
