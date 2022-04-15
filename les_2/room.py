import cv2 as cv
import numpy as np

names = np.array(['room4.jpg', 'room1.jpg', 'room2.jpg', 'room3.jpg'])
exposures = np.array([1/1000, 1/600, 1/200, 1/100], dtype= np.float32)*1000

images = []
for n in names:
    images.append(cv.imread(n))

response = cv.createCalibrateDebevec().process(images, exposures)

merge = cv.createMergeDebevec()
hdr = merge.process(images, exposures, response)

hdr = cv.resize(hdr, None, fx=0.5, fy=0.5)
cv.imshow('room', hdr)
cv.waitKey(2000)
cv.destroyAllWindows()
