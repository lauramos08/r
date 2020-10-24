import cv2
import numpy as np
import sys
import os
""" Indexing/slicing and split/merge of color components 

    python slicing.py <path_to_image> <image_name>
"""

if __name__ == '__main__':
    path = sys.argv[1]
    image_name = sys.argv[2]
    path_file = os.path.join(path, image_name)

    # Read the image
    image = cv2.imread(path_file)
    assert image is not None, "There is no image at {}".format(path_file)

    # Gray image
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # indexing/slicing
    first_pixel = image_gray[0, 0]
    last_pixel = image_gray[-1, -1]
    first_row = image_gray[0, :]
    first_column = image_gray[:, 0]
    image_rect = image_gray[100:200, 100:200]

    # split and merge
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(image_hsv)
    s = 255 * np.ones_like(s)
    v = 255 * np.ones_like(v)
    image_hue = cv2.merge((h, s, v))
    image_hue_bgr = cv2.cvtColor(image_hue, cv2.COLOR_HSV2BGR)

    # set two last components to 255
    image_hsv[..., 1:] = 255
    image_hue = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow("Image", image_hue)
    cv2.waitKey(0)
