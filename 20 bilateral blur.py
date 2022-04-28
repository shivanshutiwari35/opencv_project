import cv2
import numpy as np

img= cv2.imread('elon.jpg', 0)
cv2.imshow('output', img)

cv2.waitKey(0)

bilateral= cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow('bilateral blur', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()