import cv2

img= cv2.imread('elon.jpg')

cv2.imshow('image',img)
cv2.waitKey(0)

cv2.imshow('rotated image', cv2.transpose(img))
cv2.waitKey(0)
cv2.destroyAllWindows()