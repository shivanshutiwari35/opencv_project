import cv2

def sketch(image):
    gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur= cv2.medianBlur(gray, 5)
    canny= cv2.Canny(blur, 10, 70)
    ret, mask=cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)

    return mask

cap= cv2.VideoCapture(0)

while True:

    ret, frame=cap.read()
    cv2.imshow('our live skecth', sketch(frame))
    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows()