# image smoothing without using blurring method

import cv2
import numpy as np
img= cv2.imread('elon.jpg',0)
cv2.imshow('output', img)
cv2.waitKey(0)

blur= cv2.blur(img, (3,3))
cv2.imshow('blurred', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
