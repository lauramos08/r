import cv2
import numpy as np
import os

if __name__ == '__main__':

    # sinusoid generation
    num_rows, num_cols = (512, 512)
    enum_rows = np.linspace(0, num_rows - 1, num_rows)
    enum_cols = np.linspace(0, num_cols - 1, num_cols)
    col_iter, row_iter = np.meshgrid(enum_cols, enum_rows)
    u, v = (10, 10)
    omega = np.sqrt(u**2 + v**2)
    #theta = np.atan(v,u)

    # sinusoid visualization
    sinusoid_image = np.sin(2 * np.pi * (u * row_iter / num_rows + v * col_iter / num_cols))
    sinusoid_image_view = (sinusoid_image.copy() + 1) / 2

    cv2.imshow("Image", sinusoid_image_view)
    cv2.waitKey(0)