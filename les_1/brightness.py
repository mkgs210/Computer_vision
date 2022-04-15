import cv2 as cv
import numpy as np

image = cv.imread(r'C:\Users\Maxim\Desktop\Faculty\start\artem.png')
image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

#print(image_hsv[:,10,2])
#image_hsv[:, :, 2] = [255 if any(i>235) else i+20 for i in image_hsv[:, :, 2]]
#print([i for j in image_hsv[:, :, 2] for i in j[:]][1000:1500])
#print([255 if i>235 else i+20 for j in image_hsv[:, :, 2] for i in j[:]][1000:1500])
#print([255 if any(i>235) else i+20 for i in image_hsv[:, :, 2]])
#print(image_hsv[:,10,2])

#mask = np.array(i<=205 for i in image_hsv[:, :, 2])
print(image_hsv)
image_hsv[:,image_hsv[:,:,2]>205] = 205
#image_hsv[:,:,2]+=50
print(image_hsv)

image_hsv = cv.cvtColor(image_hsv, cv.COLOR_HSV2BGR)
cv.imshow('image', image)
cv.imshow('image_hsv', image_hsv)
cv.waitKey(1000)
cv.destroyAllWindows()