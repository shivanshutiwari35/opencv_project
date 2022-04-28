## best for blurring things out

import cv2
import numpy as np

img= cv2.imread('elon.jpg', 0)
cv2.imshow('output', img)

cv2.waitKey(0)

gaussian= cv2.GaussianBlur(img, (3,3),0)            # 3,3 is kernel and it should be in odd only.
cv2.imshow('blur', gaussian)

cv2.waitKey(0)
cv2. destroyAllWindows()