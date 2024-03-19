import cv2
import sys

img = cv2.imread('road_sign.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny_img = cv2.Canny(img, 600, 650)

circles = cv2.HoughCircles(canny_img, cv2.HOUGH_GRADIENT, 1, 10, param1=700, param2=50, minRadius=20, maxRadius=60)

if circles is None:
    print('Circle(s) not detected.')
    sys.exit()

for (x, y, r) in circles[0]:
    cv2.circle(img, (int(x), int(y)), int(r), (0, 255, 0), 6)

cv2.imshow('detected circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
