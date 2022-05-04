import cv2 as cv
import numpy as np

#избавляемся от дырок

image = cv.imread('spoons_gaps.png',0)

kernel = np.array([[0,1,0,1,0],
                   [1,1,0,1,1],
                   [0,1,0,1,0]], dtype=np.uint8) #матрица любая но обычно это квадрат или крест

dilate = cv.dilate(image, kernel)
dilate3 = cv.dilate(image, kernel, iterations=3)

cv.imshow('dilate', np.concatenate((image, dilate, dilate3), axis=1))

cv.imwrite('new_spoons_without_gaps.png', np.concatenate((image, dilate, dilate3), axis=1))
cv.waitKey(2000)
cv.destroyAllWindows()