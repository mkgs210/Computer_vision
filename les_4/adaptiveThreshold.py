import cv2 as cv
import numpy as np

text = cv.imread('text.tiff', cv.IMREAD_GRAYSCALE)
text = cv.resize(text, None, fx=0.7, fy=0.7)
#text = cv.GaussianBlur(text, (7, 7), 0)
threshold_text = cv.adaptiveThreshold(text,
                                      255,
                                      cv.ADAPTIVE_THRESH_MEAN_C,
                                      cv.THRESH_BINARY,
                                      91,#вычитается из найденного среднего по области
                                      0)


cv.imshow('text', text)
cv.imshow('threshold_text', threshold_text)
cv.waitKey(2000)
cv.destroyAllWindows()