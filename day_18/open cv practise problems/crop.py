import cv2
import os
img=cv2.imread("sample images/img1.jpeg")
crop=img[300:900,300:500]  #height:new height,width:new width
cv2.imshow("croped",crop)
cv2.imwrite("croped_img.jpg",crop)
cv2.waitKey(0)
cv2.destroyAllWindows()