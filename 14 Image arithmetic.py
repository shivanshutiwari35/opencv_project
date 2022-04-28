import cv2
import numpy as np

img= cv2.imread("elon.jpg")

M=np.ones(img.shape, dtype='uint8')*150

added=cv2.add(img, M)
subt= cv2.subtract(img,M)
mul= cv2.multiply(img,M)

cv2.imshow('added', added)
cv2.imshow('subt', subt)
cv2.imshow('prod', mul)
cv2.waitKey(0)
cv2. destroyAllWindows()


