import cv2 as cv
import numpy as np

image = np.zeros((640,1080,3), dtype=np.uint8)
h, w = image.shape[:2]

cv.rectangle(image, (100, 100), (300, 150), (0,255,0), 3)#x, y
cv.circle(image, (w//2, h//2), 100, (255,0,0), -1)

cv.putText(image, 'Hello, world', (w//2, h//4), cv.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2)
cv.imshow('image', image)
cv.waitKey(5000)
cv.destroyAllWindows()

