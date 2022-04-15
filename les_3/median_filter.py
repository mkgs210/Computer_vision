import cv2 as cv

image = cv.imread('mount.png')

median = cv.medianBlur(image, 5) #
median2 = cv.medianBlur(median, 5)
median3 = cv.medianBlur(median2, 5)

cv.imshow('mount', image)
cv.imshow('mountBlur', median)
cv.imshow('mountBlur2', median2)
cv.imshow('mountBlur3', median3) #Чем чаще тем меньше деталей
cv.waitKey(2000)
cv.destroyAllWindows()