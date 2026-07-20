import cv2
import numpy as np
img=cv2.imread("output images/grayscale.jpg")
blur=cv2.GaussianBlur(img,(9,9),0)
canny=cv2.Canny(blur,100,200)
cv2.imshow("canny",canny)
cv2.imwrite("output images/canny.jpg",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()