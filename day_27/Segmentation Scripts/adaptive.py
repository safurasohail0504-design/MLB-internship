import cv2
image = cv2.imread("Sample Input Images/document1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
adaptive = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imwrite("Output Images/document1_adaptive.jpg",adaptive)