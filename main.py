import cv2
import numpy as np
import sys
import os
from fft_show import FFT

if __name__ == '__main__':
    path = sys.argv[1]
    image_name = sys.argv[2]
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)

    fft = FFT(image, 1024)
    fft.display()

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    first_row = image_gray[0, :]
    first_column = image_gray[:, 0]
    rect = image_gray[100:200, 100:200]
    rect = np.zeros(rect.shape, np.uint8)

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(image_hsv)
    s = 255 * np.ones_like(s)
    v = 255 * np.ones_like(v)
    image_hue = cv2.merge((h, s, v))
    image_hue = cv2.cvtColor(image_hue, cv2.COLOR_HSV2BGR)

    #image_hsv[..., 1:] = 255
    image_hue = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

    image_YCrCb = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
    #hist = cv2.calcHist([image_YCrCb], [0], None, [256], [0, 256])
    #plt.plot(hist, color='gray')
    #plt.xlim([0, 256])
    #plt.show()

    ret, Ibw_Cb = cv2.threshold(image_YCrCb[...,2], 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    ret, Ibw_sat = cv2.threshold(image_hsv[...,1], 128, 255, cv2.THRESH_BINARY)


    hist = cv2.calcHist([image_hsv], [0], Ibw_Cb, [180], [0, 180])
    # plt.plot(hist, color='gray')
    # plt.xlim([0, 256])
    # plt.show()

    # Hue histogram max and location of max
    max_val = hist.max()
    max_pos = int(hist.argmax())

    # plate
    lim_inf = (max_pos - 10, 0, 0)
    lim_sup = (max_pos + 10, 255, 255)
    mask_plate = cv2.inRange(image_hsv, lim_inf, lim_sup)

    # mask
    mask = cv2.bitwise_and(mask_plate, Ibw_sat)

    cv2.imshow("Image", mask)
    cv2.waitKey(0)




