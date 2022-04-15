import cv2 as cv
import numpy as np

plane = cv.imread('plane.jpg')[50:310]
plane = cv.resize(plane, None, fx=0.35, fy=0.35, interpolation=cv.INTER_CUBIC)
plane = cv.flip(plane, 1)
square = cv.imread('square.jpg')

x=180
y=30
square[y:y+plane.shape[0],x:x+plane.shape[1],:] = plane

cv.imshow('plane', square)
cv.waitKey(2000)
cv.destroyAllWindows()