import cv2 as cv

image = cv.imread('unknown.png')

image[:,:,:] = 255 - image[:,:,:]

cv.imshow('car', image)
cv.waitKey(2000)
cv.destroyAllWindows()
