import cv2
image = cv2.imread("Sample Input Images/document1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
foreground = cv2.bitwise_and(image,image,mask=mask)
cv2.imwrite("Output Images/document1_foreground.jpg",foreground)