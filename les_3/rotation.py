import cv2 as cv
import numpy as np

image = cv.imread('room2.jpg')
image = cv.resize(image, None, fx=0.5, fy=0.5)
r_mat = cv.getRotationMatrix2D((image.shape[1]//2, image.shape[0]//2), 45, 1)

rotation = cv.warpAffine(image, r_mat, image.shape[:2])

cv.imshow('rotation', rotation)
cv.waitKey(2000)
cv.destroyAllWindows()