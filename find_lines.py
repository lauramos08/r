import os
from hough import hough
from orientation_estimate import *
import cv2

if __name__ == '__main__':
    path = '/Users/julian.quiroga/Downloads/imagenes_vision_puj/imagenes'
    image_name = 'soccer_game.png'
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)

    high_thresh = 300
    bw_edges = cv2.Canny(image, high_thresh * 0.3, high_thresh, L2gradient=True)

    hough = hough(bw_edges)
    accumulator = hough.standard_HT()

    acc_thresh = 50
    N_peaks = 11
    nhood = [25, 9]
    peaks = hough.find_peaks(accumulator, nhood, acc_thresh, N_peaks)

    [_, cols] = image.shape[:2]
    image_draw = np.copy(image)
    for i in range(len(peaks)):
        rho = peaks[i][0]
        theta_ = hough.theta[peaks[i][1]]

        theta_pi = np.pi * theta_ / 180
        theta_ = theta_ - 180
        a = np.cos(theta_pi)
        b = np.sin(theta_pi)
        x0 = a * rho + hough.center_x
        y0 = b * rho + hough.center_y
        c = -rho
        x1 = int(round(x0 + cols * (-b)))
        y1 = int(round(y0 + cols * a))
        x2 = int(round(x0 - cols * (-b)))
        y2 = int(round(y0 - cols * a))

        if np.abs(theta_) < 80:
            image_draw = cv2.line(image_draw, (x1, y1), (x2, y2), [0, 255, 255], thickness=2)
        elif np.abs(theta_) > 100:
            image_draw = cv2.line(image_draw, (x1, y1), (x2, y2), [255, 0, 255], thickness=2)
        else:
            if theta_ > 0:
                image_draw = cv2.line(image_draw, (x1, y1), (x2, y2), [0, 255, 0], thickness=2)
            else:
                image_draw = cv2.line(image_draw, (x1, y1), (x2, y2), [0, 0, 255], thickness=2)

    cv2.imshow("frame", bw_edges)
    cv2.imshow("lines", image_draw)
    cv2.waitKey(0)
