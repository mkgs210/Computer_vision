import cv2 as cv
import numpy as np

UFO = cv.imread('UFO.png',0)
UFO = cv.medianBlur(UFO, 25)
UFO = cv.resize(UFO, None, fx=0.35, fy=0.35, interpolation=cv.INTER_CUBIC)
UFO = cv.flip(UFO, 1)
kremlin = cv.imread('kremlin.jpg',0)

x=800
y=100
kremlin[y:y+UFO.shape[0],x:x+UFO.shape[1]] = UFO

cv.imshow('UFO', kremlin)
cv.waitKey(2000)
cv.destroyAllWindows()