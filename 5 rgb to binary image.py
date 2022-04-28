# images which have only black and white color

import cv2

img= cv2.imread("elon.jpg", 0)

cv2.imshow("gray", img)

cv2.waitKey(0)

ret, bw= cv2.threshold(img, 127, 150, cv2.THRESH_BINARY)

cv2.imshow("binary", bw)

cv2.waitKey(0)

cv2.destroyAllWindows()