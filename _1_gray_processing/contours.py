import cv2
import os
import sys
""" Contours (use shapes.png as example)

    python contours.py <path_to_image> <image_name>
"""

if __name__ == '__main__':
    path = sys.argv[1]
    image_name = sys.argv[2]
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)
    image_draw = image.copy()
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, Ibw_shapes = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(Ibw_shapes, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for idx, i in enumerate(contours):
        color = (0, 255, 255)
        print(len(contours[idx]))
        cv2.drawContours(image_draw, contours, idx, color, 5)

    cv2.imshow("Image", image_draw)
    cv2.waitKey(0)
