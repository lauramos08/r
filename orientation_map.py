import os
from orientation_estimate import *

if __name__ == '__main__':
    path = '/Users/julian.quiroga/Downloads/imagenes_vision_puj/imagenes'
    image_name = 'soccer_game.png'
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    [theta_data, M] = gradient_map(image_gray)
    # [theta_data, M] = orientation_map(image_gray, 7)
    theta_data += np.pi / 2
    theta_data /= np.pi
    theta_uint8 = theta_data * 255
    theta_uint8 = np.uint8(theta_uint8)
    theta_uint8 = cv2.applyColorMap(theta_uint8, cv2.COLORMAP_JET)
    theta_view = np.zeros(theta_uint8.shape)
    theta_view = np.uint8(theta_view)
    theta_view[M > 0.2] = theta_uint8[M > 0.2]

    cv2.imshow("Image", theta_view)
    cv2.waitKey(0)
