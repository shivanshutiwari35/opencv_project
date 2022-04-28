import cv2

cap= cv2.VideoCapture(0)

while True:
    ret, frame= cap.read(None)

    cv2.imshow('our live sketch', frame)

    if cv2.waitKey(1)==13:                 # 13 is the ASCII code of enter key
        break

cap.release()
cv2.destroyAllWindows()

