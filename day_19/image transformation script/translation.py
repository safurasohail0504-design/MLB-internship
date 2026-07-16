import cv2
import numpy as np
img=cv2.imread("C:/Users/User/Documents/GitHub/day_19/input images/sample_translation.jpeg")
height,width,channel=img.shape
matrix1=np.float32([[1,0,150],[0,1,0]])
matrix2=np.float32([[1,0,0],[0,1,80]])
horizontal=cv2.warpAffine(img,matrix1,(width,height))
vertical=cv2.warpAffine(img,matrix2,(width,height))
cv2.imshow("Original",img)
cv2.imshow("horizontal",horizontal)
cv2.imshow("vertical",vertical)
cv2.imwrite("horizontal_translated.jpg",horizontal)
cv2.imwrite("vertical_translated.jpg",vertical)
cv2.waitKey(0)
cv2.destroyAllWindows