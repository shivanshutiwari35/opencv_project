import cv2
import numpy as np

img= cv2.imread('elon.jpg', 0)
cv2.imshow('output', img)

cv2.waitKey(0)

laplacina= cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow('laplacian', laplacina)

cv2.waitKey(0)
cv2.destroyAllWindows()
