import cv2
import numpy as np
img=cv2.imread("C:/Users/User/Documents/GitHub/day_19/sample_translation.jpeg")
height,width,chanel=img.shape
matrix1=cv2.getRotationMatrix2D((width/2,height/2),30,0.9)
matrix2=cv2.getRotationMatrix2D((width/2,height/2),45,1)
matrix3=cv2.getRotationMatrix2D((width/2,height/2),60,0.9)
rotate30=cv2.warpAffine(img,matrix1,(width,height))
rotate45=cv2.warpAffine(img,matrix2,(width,height))
rotate60=cv2.warpAffine(img,matrix3,(width,height))
cv2.imshow("Original",img)
cv2.imshow("rotated_30",rotate30)
cv2.imshow("rotated_45",rotate45)
cv2.imshow("rotated_60",rotate60)
cv2.imwrite("rotated_30.jpg",rotate30)
cv2.imwrite("rotated_45.jpg",rotate45)
cv2.imwrite("rotated_60.jpg",rotate60)
cv2.waitKey(0)
cv2.destroyAllWindows
