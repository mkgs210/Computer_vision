import cv2 as cv

image = cv.imread("building.jpg")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
sift = cv.SIFT_create()
gray = cv.GaussianBlur(gray, (13,13), 0)
keyPoints = sift.detect(gray, None)
cv.drawKeypoints(image, keyPoints, image, (0,0,255))

cv.imshow('sift', cv.resize(image, None, fx=1, fy=1))
cv.waitKey(2000)
cv.destroyAllWindows()