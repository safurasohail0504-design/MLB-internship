import cv2
image=cv2.imread("Sample Input Images/vehicle.jpeg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()