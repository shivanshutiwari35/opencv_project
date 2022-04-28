import cv2

img = cv2.imread('elon.jpg')

cv2.imshow('original', img)

cv2.waitKey(0)

re_img= cv2.resize(img,None, fx=0.75, fy= 0.75, interpolation=None)
cv2.imshow("resized", re_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# for doubling the size of image

d_img= cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

cv2.imshow("doubled image",d_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# for giving exact dimension we give tuple value at the place of None and no need of fx and fy

a_img= cv2.resize(img, (900,400), interpolation=cv2.INTER_AREA)
cv2.imshow("area image", a_img)
cv2.waitKey(0)
cv2.destroyAllWindows()