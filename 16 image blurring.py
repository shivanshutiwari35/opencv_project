# image blurring for clear edges and smoothening effect
import cv2
import numpy as np

img= cv2.imread('elon.jpg', 0)
cv2.imshow('original', img)

# this kernel is created that actually just stretch the particular pixels by creating kernel and dividing by 9 to take
# only the required size of the stretched image and not the whole

kernel_10x10= np.ones((3,3), np.float32)/9
blurred= cv2.filter2D(img, -1,kernel_10x10)

cv2.imshow("blurred 1", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()
