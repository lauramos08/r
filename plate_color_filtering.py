import cv2
import numpy as np
import os

if __name__ == '__main__':
    path = '/Users/julian.quiroga/Downloads/imagenes_vision_puj/imagenes'
    image_name = 'placa3.png'
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image_YCrCb = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)

    ret, Ibw_Cb = cv2.threshold(image_YCrCb[..., 2], 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    hist = cv2.calcHist([image_hsv], [0], Ibw_Cb, [180], [0, 180])

    # Hue histogram max and location of max
    max_val = hist.max()
    max_pos = int(hist.argmax())

    # plate
    lim_inf = (max_pos - 10, 0, 0)
    lim_sup = (max_pos + 10, 255, 255)
    mask_plate = cv2.inRange(image_hsv, lim_inf, lim_sup)

    # mask
    ret, Ibw_sat = cv2.threshold(image_hsv[..., 1], 128, 255, cv2.THRESH_BINARY)
    mask = cv2.bitwise_and(mask_plate, Ibw_sat)
    mask_ = np.logical_and(mask_plate, Ibw_sat)

    W = 1
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2 * W + 1, 2 * W + 1))
    mask_eroded = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    W = 5
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2 * W + 1, 2 * W + 1))
    mask_dilated = cv2.morphologyEx(mask_eroded, cv2.MORPH_CLOSE, kernel)

    cv2.imshow("Image", mask_dilated)
    cv2.waitKey(0)
