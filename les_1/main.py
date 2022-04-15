import numpy as np
import cv2
img1 = np.ones((480,640), dtype = np.uint8)*255

#cv2.namedWindow("image1", cv2.WINDOW_NORMAL)
#cv2.imshow("image1", img1)


img = cv2.imread(r'C:\Users\Maxim\Desktop\Faculty\start\artem.png')# ,0 for black-white
height, weight = img.shape[:2]
print(height, weight)
#print(img)

'''for x in range(weight):
    for y in range(height):
        if x%2==0 and y%2==0:
            img[y, x] = 0'''

img[height//2+20: height//2+40, weight//2-100:weight//2+10] = (255,255,0)

cv2.imshow("image2", img)
cv2.waitKey(0)
cv2.destroyAllWindows()