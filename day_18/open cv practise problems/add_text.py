import cv2
img=cv2.imread("sample images/img1.jpeg")
cv2.putText(img,"Safura Sohail",(40,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
cv2.putText(img,"15 July 2026",(40,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
cv2.imshow("text",img)
cv2.imwrite("text.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()