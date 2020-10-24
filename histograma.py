import cv2
import os
from matplotlib import pyplot as plt

if __name__ == '__main__':
    path = '/Users/julian.quiroga/Downloads/imagenes_vision_puj/imagenes'
    image_name = 'lena.png'
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)

    # Gray levels histogram
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([image_gray], [0], None, [256], [0, 256])
    plt.plot(hist, color='gray')
    plt.xlim([0, 256])
    plt.show()

    # Hue component histogram
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist_hsv = cv2.calcHist([image_hsv], [0], None, [180], [0, 180])
    plt.plot(hist_hsv, color='red')
    plt.xlim([0, 180])
    plt.show()

    # Histogram equalization
    image_gray_equalized = cv2.equalizeHist(image_gray)
