import cv2

framewidth = 640       # height and width of the screen which will be shown to us.
frameHeight = 360

cap = cv2.VideoCapture("location of video in resources")   # location of the video is to be passed
                                                            # 0 can also be passed for web cam

while True:

    rev, img = cap.read()
    img = cv2.resize(img, (framewidth, frameHeight))    # this function is used for resizing the image

    cv2.imshow("video", img)

    if cv2.waitKey(1)==13:
        break

cv2.release()
cv2.destroyAllWindows()