import cv2 as cv
import numpy as np


bolts = cv.imread('bolts.jpg', 0)
bolts = cv.resize(bolts, None, fx=2, fy=2)
image = cv.GaussianBlur(bolts, (7, 7), 0)
_, threshold = cv.threshold(bolts, 127, 255, cv.THRESH_BINARY)#RIGHT example
cv.imshow('bolts', bolts)
cv.imshow('threshold_bolts', threshold)

text = cv.imread('text.tiff')
text = cv.resize(text, None, fx=0.7, fy=0.7)
#text = cv.GaussianBlur(text, (7, 7), 0)
_, threshold_text = cv.threshold(text, 127, 255, cv.THRESH_BINARY)#WRONG example
cv.imshow('text', text)
cv.imshow('threshold_text', threshold_text)

'''WHAT YOU NEED TO DO CHECK IN adaptiveThreshold.py'''
cv.waitKey(2000)
cv.destroyAllWindows()