import cv2 as cv
import numpy as np

#избавляемся от дырок не меняя размер ложек на изображении, для этого использвуем оба метода по очереди

spoons_gaps = cv.imread('spoons_gaps.png',0)
spoons_noise = cv.imread('spoons_noise.png',0)

kernel = cv.getStructuringElement(cv.MORPH_CROSS, (5,5))

new_spoons_gaps = cv.morphologyEx(spoons_gaps, cv.MORPH_CLOSE, kernel, iterations=3)
new_spoons_noise = cv.morphologyEx(spoons_noise, cv.MORPH_OPEN, kernel, iterations=3)

cv.imshow('close(dilate+erode)', np.concatenate((spoons_gaps, new_spoons_gaps), axis=1))
cv.imshow('open(erode+dilate)', np.concatenate((spoons_noise, new_spoons_noise), axis=1))

cv.imwrite('close(dilate+erode).png', np.concatenate((spoons_gaps, new_spoons_gaps), axis=1))
cv.imwrite('open(erode+dilate).png', np.concatenate((spoons_noise, new_spoons_noise), axis=1))
cv.waitKey(2000)
cv.destroyAllWindows()