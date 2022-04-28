# image resizing using pyramid to half or double the image size directly without knowing the dimensions

import cv2

img= cv2.imread("elon.jpg")

smaller= cv2.pyrDown(img)
larger = cv2.pyrUp(img)

cv2.imshow("original", img)
cv2.imshow("smaller", smaller)
cv2.imshow("larger", larger)

cv2.waitKey(0)
cv2.destroyAllWindows()
