import cv2
import numpy as np
import os
import sys
from _3_Fourier_analysis.fft_show import FFT

""" Simple high-pass filter

    python high_pass_filtering.py <path_to_image> <image_name>
"""

if __name__ == '__main__':
    path = sys.argv[1]
    image_name = sys.argv[2]
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    kernel = np.array([[-0.5, 0, 0.5]])
    image_filtered = cv2.filter2D(image_gray, -1, kernel)

    fft_kernel = FFT(kernel, 512)
    fft_kernel.display()
