import cv2 as cv

img = cv.imread('sunflowers.png')

params = cv.SimpleBlobDetector_Params()
params.filterByArea = False
params.maxArea = 3500
params.filterByConvexity = False
params.minConvexity = 0.97
params.filterByInertia = False
params.minInertiaRatio = 0.9
params.filterByCircularity = False
params.minCircularity = 0.9
detector = cv.SimpleBlobDetector_create()#params)

keyPoints = detector.detect(img)
cv.drawKeypoints(img, keyPoints, img, (0,0,255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv.imshow('blob', cv.resize(img, None, fx=1, fy=1))
cv.waitKey(2000)
cv.destroyAllWindows()