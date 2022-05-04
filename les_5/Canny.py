import cv2 as cv

img = cv.imread('building.jpg',0)
img = cv.GaussianBlur(img, (3,3), 0)

Canny = cv.Canny(img, 100, 200)
cv.imshow('Canny', Canny)
cv.waitKey(2000)
cv.destroyAllWindows()