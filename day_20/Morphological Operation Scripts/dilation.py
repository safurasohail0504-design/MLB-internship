import cv2
import numpy as np
img=cv2.imread("output images/grayscale.jpg",0)
kernel=np.ones((5,5),np.uint8)
dilation=cv2.dilate(img,kernel,iterations=1)
cv2.imshow("Original",img)
cv2.imshow("dilation",dilation)
cv2.imwrite("output images/dilation.jpg",dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()