import cv2
import numpy as np
import os

if __name__ == '__main__':
    path = '/Users/julian.quiroga/Downloads/imagenes_vision_puj/imagenes'
    image_name = 'lena.png'
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 1) interpolation
    # insert zeros
    rows, cols = image_gray.shape
    num_of_zeros = 5
    image_zeros = np.zeros((num_of_zeros * rows, num_of_zeros * cols), dtype=image_gray.dtype)
    image_zeros[::num_of_zeros, ::num_of_zeros] = image_gray
    W = 2 * num_of_zeros + 1
    image_interpolated = cv2.GaussianBlur(image_zeros, (W, W), 0)
    image_interpolated *= num_of_zeros ** 2

    # decimate
    image_decimated = image_gray[::2, ::2]

    # resizing with opencv
    image_resized = cv2.resize(image_gray, (256, 256))

    cv2.imshow("Image", image_resized)
    cv2.waitKey(0)
