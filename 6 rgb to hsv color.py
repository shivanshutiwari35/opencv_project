import cv2

img = cv2.imread('elon.jpg')

hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("hsv image", hsv)

cv2.imshow('hue channel', hsv[:, :, 0])
cv2.imshow('saturation channel', hsv[:, :, 1])
cv2.imshow('value channel', hsv[:, :, 2])

cv2.waitKey(0)

cv2.destroyAllWindows()
