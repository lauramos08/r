import cv2
import numpy as np

""" 2D sinusoid generation and visualization

    python sinusoid2D.py
"""

if __name__ == '__main__':
    # image parameters
    num_rows = 512
    num_cols = 512
    u, v = (10, 10)

    # sinusoid generation
    enum_rows = np.linspace(0, num_rows - 1, num_rows)
    enum_cols = np.linspace(0, num_cols - 1, num_cols)
    col_iter, row_iter = np.meshgrid(enum_cols, enum_rows)
    sinusoid_image = np.sin(2 * np.pi * (u * row_iter / num_rows + v * col_iter / num_cols))

    omega = np.sqrt(u ** 2 + v ** 2)
    theta = np.atan(v, u)

    # sinusoid visualization
    sinusoid_image_view = (sinusoid_image.copy() + 1) / 2

    cv2.imshow("Image", sinusoid_image_view)
    cv2.waitKey(0)
