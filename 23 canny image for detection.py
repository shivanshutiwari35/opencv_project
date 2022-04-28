import cv2
import numpy as np

img= cv2.imread('elon.jpg', 0)
cv2.imshow('output', img)

cv2.waitKey(0)

canny= cv2.Canny(img, 50, 170)   # the number passed as argument is for finding the correct border size
cv2.imshow("canny", canny)
cv2.waitKey(0)
canny= cv2.Canny(img, 250, 170)
cv2.imshow("canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

