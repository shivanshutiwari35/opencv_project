import cv2

img = cv2.imread('elon.jpg')

cv2.imshow('output elon', img) 

cv2.waitKey(0)     # for delaying the output, for infinte time 0 is given else give number of seconds in the arg.

cv2.destroyAllWindows()     # to destroy windows

# another way of reading image frm some location is

#img = cv2.imread('C:/Users/shiva/PycharmProjects/opencv_learn/elon.jpg')