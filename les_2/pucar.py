import cv2 as cv

image = cv.imread('r.png')+cv.imread('g.png')+cv.imread('b.png')[:,:-1,:]
image = cv.resize(image, None, fx=3, fy=3) #увеличиваем изображение в 3 раза

cv.imshow('car', image)
cv.waitKey(2000)
cv.destroyAllWindows()
