import cv2
import numpy as np

img=cv2.imread("elon.jpg")

cv2.waitKey(0)
height, width = img.shape[:2]
print(height)
print(width)

q_height = height/4
q_width = width/4

T= np.float32([[1, 0, q_height],[0, 1, q_width]])

translated=cv2.warpAffine(img, T, (width, height))


cv2.imshow("translate", translated)

cv2.waitKey(0)

cv2.destroyAllWindows()