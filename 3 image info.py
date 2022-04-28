import cv2

img = cv2.imread('elon.jpg')

cv2.imshow('output elon', img)
print(img.shape)
print("height of image: ",img.shape[0])
print("width of image: ",img.shape[1])
print(img.shape[2])

cv2.waitKey(0)

cv2.destroyAllWindows()
