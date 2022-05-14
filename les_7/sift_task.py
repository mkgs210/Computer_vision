import cv2 as cv

img = cv.imread('box_in_scene.png',0)
template = cv.imread('box.png',0)

sift = cv.SIFT_create()
kP_template, des_template = sift.detectAndCompute(template, None)
kP_img, des_img = sift.detectAndCompute(img, None)

bf = cv.BFMatcher()
matches = bf.knnMatch(des_template, des_img, k=2)
good_matches = []
for m, n in matches:
    if m.distance <0.75*n.distance:
        good_matches.append([m])

img_result = cv.drawMatchesKnn(template, kP_template, img, kP_img, good_matches, None, flags=2)

cv.imshow('sift', cv.resize(img_result, None, fx=1, fy=1))
cv.waitKey(2000)
cv.destroyAllWindows()