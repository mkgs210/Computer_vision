import cv2 as cv
import numpy as np

img = cv.imread('coins1.jpg')
blur = cv.GaussianBlur(img, (7,7), 0)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
upper = (17, 160, 255)
lower = (13, 110, 20)

canny = cv.Canny(blur, 70, 235)
contours, _ = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

for i in contours:
    (x,y), radius = cv.minEnclosingCircle(i)
    if 30<radius<70:
        mask = np.zeros(img.shape[:2],dtype=np.uint8)
        cv.circle(mask, (int(x), int(y)), int(radius), 255, -1)
        average = cv.mean(hsv, mask)

        if  lower[0]<average[0]<upper[0] and lower[1]<average[1]<upper[1] and lower[2]<average[2]<upper[2]:
            print(average)
            cv.circle(img, (int(x), int(y)), int(radius), (0,255,0), 2)

cv.imshow('Canny', canny)
cv.imshow('img', img)
cv.waitKey(2000)
cv.destroyAllWindows()