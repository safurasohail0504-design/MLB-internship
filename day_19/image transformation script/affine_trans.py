import cv2
import numpy as np
img=cv2.imread("C:/Users/User/Documents/GitHub/day_19/sample_translation.jpeg")
height,width,chanel=img.shape
p1=np.float32([[100,50],[680,50],[100,320]])
p2=np.float32([[50,100],[700,30],[180,350]])
matrix=cv2.getAffineTransform(p1,p2)
affined=cv2.warpAffine(img,matrix,(width,height))
cv2.imshow("Original",img)
cv2.imshow("affined",affined)
cv2.imwrite("affine_trans.jpg",affined)
cv2.waitKey(0)
cv2.destroyAllWindows
