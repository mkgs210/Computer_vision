import cv2 as cv
import numpy as np

car = cv.imread('car.jpg')
road = cv.imread('road.jpg')

result = cv.addWeighted(road, 0.2, car, 0.9, 0)

cv.imshow('result', result)
cv.waitKey(2000)
cv.destroyAllWindows()