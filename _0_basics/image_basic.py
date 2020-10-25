import cv2
import sys
import os
""" Read and show and image with opencv

    python image_basic.py <path_to_image> <image_name>
"""

if __name__ == '__main__':
    path = sys.argv[1]
    image_name = sys.argv[2]
    path_file = os.path.join(path, image_name)

    # Read the image
    image = cv2.imread(path_file)

    # Check the image is valid
    assert image is not None, "There is no image at {}".format(path_file)

    # Show the image
    cv2.imshow("Image", image)
    cv2.waitKey(0)




