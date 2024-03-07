import cv2
import numpy as np

drawing = False
ix = -1
iy = -1


def draw_rectangle(event, x, y, flags, params):

    global drawing, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(canvas, (ix, iy), (x, y), (255, 0, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(canvas, (ix, iy), (x, y), (255, 0, 0), -1)

cv2.namedWindow(winname="mydrawing")
canvas = np.zeros((500, 500, 3), np.int8)

cv2.setMouseCallback("mydrawing", draw_rectangle)

while True:
    cv2.imshow("mydrawing", canvas)

    if cv2.waitKey(20) & 0xff == 27:
        break

cv2.destroyAllWindows()
