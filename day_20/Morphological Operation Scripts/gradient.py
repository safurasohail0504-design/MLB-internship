import cv2
import numpy as np
img=cv2.imread("output images/grayscale.jpg",0)
kernel=np.ones((5,5),np.uint8)
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
cv2.imshow("Original",img)
cv2.imshow("gradient",gradient)
cv2.imwrite("output images/gradient.jpg",gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()