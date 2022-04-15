import cv2 as cv
import numpy as np

image = cv.imread('room2.jpg')
image = cv.resize(image, None, fx=0.5, fy=0.5)

flipped = cv.flip(image, 1)


cv.imshow('image', image)
cv.imshow('flipped', flipped)
cv.waitKey(2000)
cv.destroyAllWindows()