import cv2 as cv
import numpy as np

image = cv.imread('room2.jpg')
image = cv.resize(image, None, fx=0.5, fy=0.5)
tx=100
ty=15
t_mat = np.array([[1,0,tx],
                  [0,1,ty]], dtype=np.float32)

translation = cv.warpAffine(image, t_mat, image.shape[:2])

cv.imshow('translation', translation)
cv.waitKey(2000)
cv.destroyAllWindows()