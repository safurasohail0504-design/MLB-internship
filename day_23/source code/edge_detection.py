import cv2
image=cv2.imread("Sample Input Images/sample_edge.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(9,9),0)
canny=cv2.Canny(blur,100,200)
cv2.imshow("Edge Detection",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()