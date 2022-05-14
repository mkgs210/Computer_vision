import cv2 as cv

image = cv.imread("building.jpg")
img = image.copy()
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
harris = cv.cornerHarris(gray, 2, 5, 0.06)

thresh = harris.max() * 0.01
image[harris>thresh] = [0, 0, 255]

gray = cv.GaussianBlur(gray, (13,13), 0)
fast = cv.FastFeatureDetector_create()

keyPoints = fast.detect(gray, None)
img = cv.drawKeypoints(img, keyPoints, None, (0,0,255))

cv.imshow('image', cv.resize(image, None, fx=1, fy=1))
cv.imshow('img', cv.resize(img, None, fx=1, fy=1))
cv.waitKey(2000)
cv.destroyAllWindows()