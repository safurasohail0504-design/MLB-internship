import cv2
import numpy as np
img=cv2.imread("C:/Users/User/Documents/GitHub/day_19/sample_translation.jpeg")
height,width,chanel=img.shape
p1=np.float32([[80,40],[700,60],[40,340],[740,350]])
p2=np.float32([[0,0],[783,0],[0,392],[783,392]])
matrix=cv2.getPerspectiveTransform(p1,p2)
Perspective=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Original",img)
cv2.imshow("Perspective",Perspective)
cv2.imwrite("Perspective_trans.jpg",Perspective)
cv2.waitKey(0)
cv2.destroyAllWindows