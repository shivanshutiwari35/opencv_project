import cv2

img = cv2.imread('elon.jpg' , 0)  # can be done directly by passing 0 for grey as the parameter if 1 then coloured in rgb

cv2.imshow('output elon', img)

cv2.waitKey(0)


cv2.destroyAllWindows()

# or

img = cv2.imread('elon.jpg')

cv2.imshow('output elon', img)

cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayone', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
