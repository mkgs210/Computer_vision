import cv2 as cv

img = cv.imread('coins1.jpg')
blur = cv.GaussianBlur(img, (7,7), 0)

canny = cv.Canny(blur, 70, 235)
contours, _ = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

for i in contours:
    (x,y), radius = cv.minEnclosingCircle(i)
    if radius>30 and radius<70:
        cv.circle(img, (int(x), int(y)), int(radius), (0,255,0), 2)

cv.imshow('Canny', canny)
cv.imshow('img', img)
cv.waitKey(2000)
cv.destroyAllWindows()