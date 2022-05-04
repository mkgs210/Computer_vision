import cv2 as cv
import numpy as np

capture = cv.VideoCapture('stepler.mp4')

while(capture.isOpened()):
    success_or_not, frame = capture.read()
    frame1 = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    threshed = cv.inRange(frame1, (110, 90, 0), (115, 255, 255))
    kernel = cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))
    threshed = cv.morphologyEx(threshed, cv.MORPH_CLOSE, kernel, iterations=5)
    threshed = cv.morphologyEx(threshed, cv.MORPH_OPEN, kernel, iterations=1)
    threshed = cv.bitwise_and(frame, frame, mask=threshed)
    #threshed = cv.cvtColor(threshed, cv.COLOR_GRAY2BGR)
    cv.imshow('stepler', threshed)
    key = cv.waitKey(10)

cv.destroyAllWindows()