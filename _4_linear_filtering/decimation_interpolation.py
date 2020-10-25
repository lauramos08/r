import cv2
import numpy as np
import os
import sys

""" Decimation, interpolation and resizing 

    python decimation_interpolation.py <path_to_image> <image_name>
"""

if __name__ == '__main__':
    path = sys.argv[1]
    image_name = sys.argv[2]
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Interpolation
    # insert zeros
    rows, cols = image_gray.shape
    num_of_zeros = 5
    image_zeros = np.zeros((num_of_zeros * rows, num_of_zeros * cols), dtype=image_gray.dtype)
    image_zeros[::num_of_zeros, ::num_of_zeros] = image_gray
    W = 2 * num_of_zeros + 1
    # filtering
    image_interpolated = cv2.GaussianBlur(image_zeros, (W, W), 0)
    image_interpolated *= num_of_zeros ** 2

    # Decimation
    D = 2
    image_decimated = image_gray[::D, ::D]

    # Resizing with opencv
    width = 256
    height = 256
    image_resized = cv2.resize(image_gray, (width, height))

    cv2.imshow("Image", image_resized)
    cv2.waitKey(0)
