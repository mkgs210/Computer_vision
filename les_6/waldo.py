import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

beach = cv.imread('WaldoBeach.jpg')
waldo = cv.imread('waldo.jpg')
beach = cv.resize(beach, None, fx=0.5, fy= 0.5)
waldo = cv.resize(waldo, None, fx=0.5, fy= 0.5)
result = cv.matchTemplate(beach, waldo, cv.TM_CCOEFF)

weight = waldo.shape[1]
hight = waldo.shape[0]

#plt.imshow(result)
#plt.show()#выводится карта откликов, нам в данном случае нужен самый яркий, мы его ищем ниже

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

cv.rectangle(beach, (max_loc[0], max_loc[1]),
             (max_loc[0]+weight, max_loc[1]+hight), (0,255,0), 2)
cv.imshow('beach', beach)
cv.imshow('waldo', cv.resize(waldo, None, fx=4, fy=4))
cv.waitKey(2000)
cv.destroyAllWindows()

