# this is for creating a clone of another image in png or jpg format

import cv2

img = cv2.imread('elon.jpg')

cv2.imshow('output elon', img)

cv2.imwrite('output.jpg', img)  # this is for creating a jpg image and
cv2.imwrite('outout.png', img)  # this is for creating png image and will be saved in the same file where project is

cv2.waitKey(0)

cv2.destroyAllWindows()