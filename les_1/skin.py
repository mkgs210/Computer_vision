import cv2 as cv
import numpy as np

image = cv.imread(r'C:\Users\Maxim\Desktop\Faculty\start\arsenal.jpg')
image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
lower = np.array([0,48,80], dtype=np.uint8)
upper = np.array([20,255,255], dtype=np.uint8)
mask = cv.inRange(image_hsv, lower, upper)
image_musked = cv.bitwise_and(image, image, mask=mask)

cv.imshow('image', image)
cv.imshow('mask', mask)
cv.imshow('image_musked', image_musked)

cv.waitKey(10000)
cv.destroyAllWindows()