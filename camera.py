import cv2

if __name__ == '__main__':
    camera = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
    ret = True
    while ret:
        ret, image = camera.read()
        if ret:
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            high_thresh = 255
            bw_edges = cv2.Canny(image_gray, high_thresh * 0.3, high_thresh, L2gradient=True)
            cv2.imshow("Image", bw_edges)
            cv2.waitKey(1)
