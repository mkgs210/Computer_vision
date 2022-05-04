import cv2 as cv
import numpy as np

aim = cv.imread('target.jpg')
aim_gray = cv.cvtColor(aim, cv.COLOR_BGR2GRAY)
cv.namedWindow('threshed')
bottom_value = 70
upper_value = 190
def onChange(value):
    global bottom_value
    global upper_value
    bottom_value = cv.getTrackbarPos('track_bottom', 'threshed')
    upper_value = cv.getTrackbarPos('track_upper', 'threshed')
    if bottom_value > upper_value:
        upper_value = bottom_value
    threshed = cv.inRange(aim_gray, bottom_value, upper_value)
    cv.imshow('threshed', threshed)

cv.createTrackbar('track_bottom', 'threshed', 0, 255, onChange)
cv.setTrackbarPos('track_bottom', 'threshed', bottom_value)
cv.createTrackbar('track_upper', 'threshed', 0, 255, onChange)
cv.setTrackbarPos('track_upper', 'threshed', upper_value)

cv.waitKey()
cv.destroyAllWindows()