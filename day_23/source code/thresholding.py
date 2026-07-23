import cv2
image=cv2.imread("Sample Input Images/vehicle.jpeg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("Thresholding",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()