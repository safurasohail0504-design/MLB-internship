import cv2
import numpy as np
img=cv2.imread("C:/Users/User/Documents/GitHub/day_19/sample_translation.jpeg")
high=cv2.convertScaleAbs(img,alpha=2,beta=0)
low=cv2.convertScaleAbs(img,alpha=0.5,beta=0)
cv2.imshow("high_contrast",high)
cv2.imshow("low_contrast",low)
cv2.imwrite("high_contrast.jpg",high)
cv2.imwrite("low_contrast.jpg",low)
cv2.waitKey(0)
cv2.destroyAllWindows