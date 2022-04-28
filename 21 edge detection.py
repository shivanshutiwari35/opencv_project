import cv2
import numpy as np

img= cv2.imread('elon.jpg', 0)
cv2.imshow('output', img)

cv2.waitKey(0)

height, width= img.shape

sobel_x= cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

sobel_y= cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow('sobel_x', sobel_x)
cv2.imshow('sobel_y', sobel_y)
cv2.waitKey(0)

combined = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow('combined',combined)
cv2.waitKey(0)
cv2.destroyAllWindows()

