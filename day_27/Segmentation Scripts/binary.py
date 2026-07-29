import cv2
image = cv2.imread("Sample Input Images/document1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
cv2.imwrite("Output Images/document1_binary.jpg",binary)