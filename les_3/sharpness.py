import cv2 as cv
import numpy as np

image = cv.imread('room2.jpg',0)
image = cv.resize(image, None, fx=0.5, fy=0.5)
#image = cv.medianBlur(image, 5)

m1 = np.array([[1,1,1],
              [1,1,1],
              [1,1,1]], dtype=np.float32)/9#Блюрим
m2 = np.array([[0,0,0],
              [0,2,0],
              [0,0,0]], dtype=np.float32)#Увеличиваем яркость в 2 раза
blur = cv.filter2D(image, None, m1)
#image = (image+(image - blur)).astype(np.uint8)

brightness = cv.filter2D(image, None, m2)
image1 = (cv.subtract(brightness, blur)).astype(np.uint8)



cv.imshow('image', image)
cv.imshow('image1', image1)#хреново работает
cv.waitKey(2000)
cv.destroyAllWindows()