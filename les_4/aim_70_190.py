import cv2 as cv
import numpy as np

aim = cv.imread('target.jpg')
aim_gray = cv.cvtColor(aim, cv.COLOR_BGR2GRAY)
aim_gray = cv.resize(aim_gray, None, fx=0.7, fy=0.7)
threshed = cv.inRange(aim_gray, 70, 190)

kernel = cv.getStructuringElement(cv.MORPH_CROSS, (5,5))

new_threshed = cv.morphologyEx(threshed, cv.MORPH_OPEN, kernel, iterations=1)
cv.imshow('threshed', np.concatenate((aim_gray, threshed, new_threshed),axis=1))
cv.waitKey()
cv.destroyAllWindows()