import cv2 as cv
import numpy as np

capture = cv.VideoCapture('stepler.mp4')
_, frame = capture.read()
black = np.zeros(frame.shape, dtype=np.uint8)
last_x=-1
last_y=-1

while True:
    ret, frame = capture.read()
    if ret == False:
        #break #для завершения без ошибок
        capture.set(cv.CAP_PROP_POS_FRAMES, 0)#а здесь мы возвращаемся к началу видео
        #black = np.zeros(black.shape, dtype=np.uint8)#и обнуляем black
        last_x = -1
        last_y = -1
        continue

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, (110, 90, 0), (115, 255, 255))

    moments = cv.moments(mask, 1)
    m01 = moments['m01']
    m10 = moments['m10']
    m00 = moments['m00']
    x = int(m10/m00)
    y = int(m01/m00)
    cv.circle(frame, (x,y), 8, (0,0,255), -1)
    if last_x>=0 and last_y>=0:
        cv.line(black, (last_x, last_y), (x,y), (0,255,0), 4)
    last_x = x
    last_y = y
    frame = cv.add(frame, black)

    cv.imshow('frame', frame)
    key = cv.waitKey(1)

    if key == 27:
        break
    if key == ord(' '):
        cv.waitKey()

cv.destroyAllWindows()