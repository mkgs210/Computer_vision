import cv2 as cv
import numpy as np

image = cv.imread('room2.jpg',0)
image = image[image.shape[0]//2:,image.shape[1]//2:]

gray=np.ones(image.shape,dtype=np.uint8)*50

bright_up = cv.add(image, gray)
bright_down = cv.subtract(image, gray)
cv.imshow('bright_up',bright_up)
cv.imshow('bright_down',bright_down)
cv.waitKey(2000)
cv.destroyAllWindows()