import cv2 as cv
from matplotlib import pyplot as plt

upper = (118, 230, 255)
lower = (108, 160, 20)
points = []
def getHist(event, x, y, flags, param):
    global points
    if event == cv.EVENT_LBUTTONDOWN:
        points = [(x,y)]
    elif event == cv.EVENT_LBUTTONUP:
        points.append((x,y,))
        cv.rectangle(frame, points[0], points[1], (0, 255, 0), 2)
        cv.imshow('frame', frame)
        roi = hsv[points[0][1]:points[1][1], points[0][0]:points[1][0]]#берем у-ки потом х-сы
        hist = cv.calcHist([roi], [0,1], None, [256, 256], [0, 255, 0, 255])
        plt.imshow(hist)
        plt.show()

capture = cv.VideoCapture('stepler.mp4')
cv.namedWindow('frame')
cv.setMouseCallback('frame', getHist)

while True:
    success_or_not, frame = capture.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    mask = cv.inRange(hsv, lower, upper)
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel, iterations=3)
    mask = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('mask', mask)

    cv.imshow('frame', frame)
    key = cv.waitKey(20)
    if key == ord('q'):
        break
    if key == ord(' '):
        cv.waitKey()

cv.destroyAllWindows()
capture.release()