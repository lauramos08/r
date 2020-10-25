import cv2
import os
import sys
""" Color filtering based on Hue histogram peak

    python color_filtering.py <path_to_image> <image_name>
"""

if __name__ == '__main__':
    path = sys.argv[1]
    image_name = sys.argv[2]
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)

    # Hue histogram
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist_hsv = cv2.calcHist([image_hsv], [0], None, [180], [0, 180])

    # Hue histogram max and location of max
    max_val = hist_hsv.max()
    max_pos = int(hist_hsv.argmax())

    # Peak mask
    lim_inf = (max_pos - 10, 0, 0)
    lim_sup = (max_pos + 10, 255, 255)
    mask = cv2.inRange(image_hsv, lim_inf, lim_sup)
    mask_not = cv2.bitwise_not(mask)

    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Image", 1280, 720)
    cv2.imshow("Image", mask_not)
    cv2.waitKey(0)
