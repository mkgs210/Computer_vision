import cv2 as cv
import numpy as np

img = cv.imread('building.jpg',0)
img = cv.GaussianBlur(img, (3,3), 0)
previt_x = np.array([[-1,-1,-1],
                    [0,0,0],
                    [1,1,1]])
previt_y = np.array([[-1,0,1],
                    [-1,0,1],
                    [-1,0,1]])

img_previt_x = cv.filter2D(img, -1, previt_x)
img_previt_y = cv.filter2D(img, -1, previt_y)
orr = cv.bitwise_or(img_previt_x, img_previt_y)#чуть лучше чем cv.add(img_previt_x, img_previt_y)

ret, thresholder = cv.threshold(orr, 90, 255, cv.THRESH_BINARY)

cv.imshow('img_previt_x',img_previt_x)
cv.imshow('img_previt_y',img_previt_y)
cv.imshow('or', orr)
cv.imshow('thresholder', thresholder)

#по идее должен работать на больших изображениях
sobel = cv.Sobel(img, -1, 1, 1, ksize=5)#по идее должен работать на больших изображениях
#по идее должен работать на больших изображениях
cv.imshow('sobel', sobel)
ret, sobel_threas = cv.threshold(sobel, 90, 255, cv.THRESH_BINARY)
cv.imshow('sobel_threas', sobel_threas)
cv.waitKey(2000)
cv.destroyAllWindows()