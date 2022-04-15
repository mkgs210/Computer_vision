import cv2 as cv
import numpy as np

square = np.zeros((300,300), dtype=np.uint8)
circle = np.zeros((300,300), dtype=np.uint8)

cv.rectangle(square, (75,75), (225,225), 255, -1)
cv.ellipse(circle, (150,150), (120,120), 30, 0, 180, 255, -1)

img_and = cv.bitwise_and(square, circle)
img_or = cv.bitwise_or(square, circle)
img_not = cv.bitwise_not(square)
img_xor = cv.bitwise_xor(square, circle)

cv.imshow('square', square)
cv.imshow('circle', circle)
cv.imshow('img_and', img_and)
cv.imshow('img_or', img_or)
cv.imshow('img_not', img_not)
cv.imshow('img_xor', img_xor)
cv.waitKey(5000)
cv.destroyAllWindows()