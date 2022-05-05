import math
import cv2 as cv
import numpy as np

img = cv.imread('hand.png')
img = cv.resize(img, None, fx=2, fy=2)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, threshold = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)

kernel = np.ones((3,3), dtype=np.uint8)
threshold = cv.morphologyEx(threshold, cv.MORPH_OPEN, kernel, iterations=5)
contours, hier = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)#контуров может быть несколько, но у нас 1 так как мы второй опенули
contours = contours[1]
hull = cv.convexHull(contours)#не работает
hull_work = cv.convexHull(contours, returnPoints=False)
cv.drawContours(img, contours, -1, (255,0,0), 2)
cv.drawContours(img, hull, -1, (0,0,255), 2)

defects = cv.convexityDefects(contours, hull_work)

count=0
for i in range(len(defects)):
    s, e, f, _ = defects[i][0]
    start = contours[s][0]
    end = contours[e][0]
    far = contours[f][0]
    a = math.sqrt((end[0]-start[0])**2 +(end[1]-start[1])**2)
    b = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
    c = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
    angle = math.acos((b**2+c**2-a**2)/(2*b*c))*57#умножаем на 57 чтобы были градусы а не радианы
    if angle<=90:
        count+=1
        cv.circle(img, (far[0], far[1]), 5, (0,255,0), -1)


cv.putText(img, 'There are' + str(count+1)+'fingers', (10,30), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))

cv.imshow('threshold', threshold)
cv.imshow('img', img)
cv.waitKey(3000)
cv.destroyAllWindows()