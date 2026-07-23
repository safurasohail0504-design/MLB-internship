import cv2
image=cv2.imread("Sample Input Images/book.jpeg")
bright=cv2.convertScaleAbs(image,beta=50)
cv2.imshow("Brightness",bright)
cv2.waitKey(0)
cv2.destroyAllWindows()