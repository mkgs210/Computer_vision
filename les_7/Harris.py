import cv2 as cv

def harris(desk, name, fx=1, fy=1):
    # desk = cv.resize(desk, None, fx=2, fy= 2)
    gray = cv.cvtColor(desk, cv.COLOR_BGR2GRAY)
    harris = cv.cornerHarris(gray, 2, 5, 0.06)
    thresh = harris.max() * 0.01
    desk[harris > thresh] = [0, 0, 255]
    cv.imshow(name, cv.resize(desk, None, fx=fx, fy=fy))


desk = cv.imread('chessb.png')
harris(desk, 'desk', 2, 2)
house = cv.imread('building.jpg')
harris(house, 'house')

cv.waitKey(2000)
cv.destroyAllWindows()

