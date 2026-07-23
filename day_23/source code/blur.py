import cv2
image=cv2.imread("Sample Input Images/person.jpeg")
blur=cv2.GaussianBlur(image,(9,9),0)
cv2.imshow("Blur",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()