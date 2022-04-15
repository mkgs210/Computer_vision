import cv2 as cv
import numpy as np

image = cv.imread('room2.jpg')
image = image[image.shape[0]//2:,image.shape[1]//2:,:]
resize_area = cv.resize(image, None,  fx=0.9, fy=0.9, interpolation=cv.INTER_AREA)
resize_nearest = cv.resize(image, None,  fx=0.9, fy=0.9, interpolation=cv.INTER_NEAREST)

p_down = cv.pyrDown(image)#Уменьшает в 2 раза
p_down = cv.pyrDown(p_down)#Еще в 2 раза
p_up = cv.pyrUp(p_down)#величивает в 2 раза
p_up = cv.pyrUp(p_up)#Еще в 2 раза

cv.imshow('image', image)
cv.imshow('resize_area', resize_area)
cv.imshow('resize_nearest', resize_nearest)
cv.imshow('p_down', p_down)
cv.imshow('p_up', p_up)
cv.waitKey(2000)
cv.destroyAllWindows()