import cv2
import os
import sys
""" Thresholding (use old_text.png as example)

    python thresholding.py <path_to_image> <image_name>
"""

if __name__ == '__main__':
    path = sys.argv[1]
    image_name = sys.argv[2]
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Manual global threshold
    threshold = 100
    ret, Ibw_manual = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)

    # Otsu's global threshold
    ret, Ibw_otsu = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Local threshold
    window_size = 51
    Ibw_local = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, window_size,
                                      0)
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Image", 1280, 720)
    cv2.imshow("Image", Ibw_local)
    cv2.waitKey(0)
