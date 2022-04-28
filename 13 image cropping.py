import cv2

img= cv2.imread("elon.jpg")
height, width= img.shape[:2]        # for gettign the value of height and width

# we require the height and width upto which we require cropped picture

start_row, start_column = int(height/4), int(width/4)

end_row, end_column = int(height*0.75), int(width*0.75)

# we are storing the part of image we require as that is done by the value of pixels

cropped=img[start_row:end_column, start_column:end_column]

cv2.imshow("original", img)
cv2.imshow("cropped", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()