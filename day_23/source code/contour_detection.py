import cv2
image=cv2.imread("Sample Input Images/sample_contour.jpeg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
output=image.copy()
for contour in contours:
    area=cv2.contourArea(contour)
    if area<500:
        continue
    cv2.drawContours(output,[contour],-1,(0,255,0),2)
cv2.imshow("Contour Detection",output)
cv2.waitKey(0)
cv2.destroyAllWindows()