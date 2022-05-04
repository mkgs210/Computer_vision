import cv2 as cv
import numpy as np

capture = cv.VideoCapture('stepler.mp4')

while True:
    success_or_not, frame = capture.read()
    frame1 = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    mask = cv.inRange(frame1, (108, 160, 20), (118, 230, 255))
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    threshed = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel, iterations=5)
    #threshed = cv.morphologyEx(threshed, cv.MORPH_OPEN, kernel, iterations=1)

    mask_frame = cv.bitwise_and(frame, frame, mask=threshed)
    cv.imshow('stepler', mask_frame)
    key = cv.waitKey(20)
    if key == ord('q'):
        break
    if key == ord(' '):
        cv.waitKey()

cv.destroyAllWindows()