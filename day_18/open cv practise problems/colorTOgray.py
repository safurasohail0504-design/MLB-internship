import cv2
img=cv2.imread("C:/Users/User/Documents/GitHub/day_18/sample images/img1.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("original",img)
cv2.imshow("converted img",gray)
cv2.imwrite("converted_gray.jpg",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()