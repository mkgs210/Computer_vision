import cv2 as cv
import numpy as np

#избавляемся от точек

image = cv.imread('spoons_noise.png',0)

kernel = cv.getStructuringElement(cv.MORPH_CROSS, (5,5))

erode = cv.erode(image, kernel)
erode3 = cv.erode(image, kernel, iterations=3)

cv.imshow('dilate', np.concatenate((image, erode, erode3), axis=1))

cv.imwrite('new_spoons_without_noise.png', np.concatenate((image, erode, erode3), axis=1))
cv.waitKey(2000)
cv.destroyAllWindows()