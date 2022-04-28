import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

print(img)
img[:] = 255, 0, 0   # for whole image make it blue (BGR)

# draw the line
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 0, 255), 2)

# for all the way for image just pass the size of the image in the second param

# draw rectangle

cv2.rectangle(img, (350,100), (450, 200), (0, 0, 255), 3)

# for filling the rectangle completely pass cv2.FILLED in place of thickness

cv2.rectangle(img, (250, 100), (325, 175), (0, 0, 255), cv2.FILLED)


# for making a circle

cv2.circle(img, (150, 400) ,(50), (0, 0, 255), cv2.FILLED)

# for adding text

cv2.putText(img, "Hello", (175, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)

cv2.imshow("Image", img)

cv2.waitKey(0)

