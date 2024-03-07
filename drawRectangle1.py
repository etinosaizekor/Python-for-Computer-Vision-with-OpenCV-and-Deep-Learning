import cv2
import numpy as np


def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img, pt1=(x, y), pt2=(x+50, y+50),
                      color=(0, 255, 0), thickness=-1)


cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing', draw_circle)

img = np.zeros((512, 512, 3), np.int8)

while True:
    cv2.imshow('my_drawing', img)

    if cv2.waitKey(20) & 0xff == 27:
        break
