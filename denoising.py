import cv2
from noise import noise
import numpy as np
import os

if __name__ == '__main__':
    path = '/Users/julian.quiroga/Downloads/imagenes_vision_puj/imagenes'
    image_name = 'lena.png'
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_gray_float = image_gray.astype(np.float)/np.max(image_gray)
    image_gray_noisy = noise("gauss", image_gray_float)
    image_gray_noisy = noise("s&p", image_gray_float)
    image_gray_noisy = noise("poisson", image_gray_float)
    image_gray_noisy = noise("speckle", image_gray_float)


    cv2.imshow("Image", image_gray_noisy)
    cv2.waitKey(0)