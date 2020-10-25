import cv2
import numpy as np
import os
import sys
from _4_linear_filtering.noise import noise

""" Visualize different types of noise

    python noising.py <path_to_image> <image_name>
"""

if __name__ == '__main__':
    path = sys.argv[1]
    image_name = sys.argv[2]
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_gray_float = image_gray.astype(np.float) / np.max(image_gray)
    image_noisy_gauss = noise("gauss", image_gray_float)
    image_noisy_sp = noise("s&p", image_gray_float)
    image_noisy_poisson = noise("poisson", image_gray_float)
    image_noisy_speckle = noise("speckle", image_gray_float)

    cv2.imshow("Image", image_noisy_gauss)
    cv2.waitKey(0)
