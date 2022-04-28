import cv2
import numpy as np

img= cv2.imread('elon.jpg', 0)
cv2.imshow('output', img)

cv2.waitKey(0)

median= cv2.medianBlur(img, 5)
cv2.imshow('median', median)

cv2.waitKey(0)
cv2.destroyAllWindows()