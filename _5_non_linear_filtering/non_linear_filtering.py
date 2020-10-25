import cv2
import numpy as np
import os
import sys
import time
from _4_linear_filtering.noise import noise

""" OpenCV non-linear filtering methods

    python non_linear_filtering.py <path_to_image> <image_name>
"""

if __name__ == '__main__':
    path = sys.argv[1]
    image_name = sys.argv[2]
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # add noise
    image_gray_noisy = noise("gauss", image_gray.astype(np.float) / 255)
    image_gray_noisy = (255 * image_gray_noisy).astype(np.uint8)

    # median
    start_time = time.time()
    image_median = cv2.medianBlur(image_gray_noisy, 7)
    elapsed_time = time.time() - start_time
    print("Median filtering: elapsed time is {} s".format(elapsed_time))

    # bilateral
    image_bilateral = cv2.bilateralFilter(image_gray_noisy, 15, 25, 25)

    # nlm
    start_time = time.time()
    image_nlm = cv2.fastNlMeansDenoising(image_gray_noisy, 3, 11, 25)
    error = image_gray.astype(np.float) - image_bilateral.astype(np.float)
    error_2 = error ** 2
    mse = np.sum(error_2) / (image_gray.shape[0] * image_gray.shape[1])
    rmse = np.sqrt(mse)
    elapsed_time = time.time() - start_time
    print(elapsed_time)

    cv2.imshow("Image", image)
    cv2.waitKey(0)
