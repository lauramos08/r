import cv2
import numpy as np
import os
from fft_show import FFT

if __name__ == '__main__':
    path = '/Users/julian.quiroga/Downloads/imagenes_vision_puj/imagenes'
    image_name = 'lena.png'
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    kernel = np.array([[-0.5, 0, 0.5]])

    fft_kernel = FFT(kernel, 512)
    fft_kernel.display()