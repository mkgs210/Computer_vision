import cv2 as cv
import numpy as np

img = cv.imread('room1.jpg')
img = cv.resize(img, None, fx=0.5, fy=0.5)
kernel = np.ones((5,5), dtype=np.float32) / 25
filterred = cv.filter2D(img, -1, kernel)#box_filter но может быть сложнее и круче

blurred = cv.blur(img, (5,5)) #простой box_filter всегда

gaus = cv.GaussianBlur(img, (7,7), 0)

cv.imshow('orig', img)
cv.imshow('gaus', gaus)
#cv.imshow('box_filter', filterred) #тоже самое что и ниже
cv.imshow('blur', blurred)


cv.waitKey(2000)
cv.destroyAllWindows()