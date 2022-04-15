import cv2 as cv
import numpy as np

image = cv.imread('dorm.png')
image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

equalize = image_hsv[:,:,:]
equalize[:,:,2] = cv.equalizeHist(image_hsv[:,:,2])

equalize = cv.resize(equalize, None, fx=2, fy=2)
cv.imshow('dorm', cv.cvtColor(equalize, cv.COLOR_HSV2BGR))


table = np.zeros(256, dtype=np.uint8)
gamma = 0.5

for i in range(256):
    table[i] = round(((i/255.)**gamma)*255)

gammed = image_hsv[:,:,:]
gammed[:,:,2] = cv.LUT(image_hsv[:,:,2], table)

gammed = cv.resize(gammed, None, fx=2, fy=2)
cv.imshow('gammed', cv.cvtColor(gammed, cv.COLOR_HSV2BGR))
cv.waitKey(2000)
cv.destroyAllWindows()