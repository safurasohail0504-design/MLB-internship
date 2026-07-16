import cv2
import numpy as np
img=cv2.imread("C:/Users/User/Documents/GitHub/day_19/sample_translation.jpeg")
gaussian=cv2.GaussianBlur(img,(9,9),0)
median=cv2.medianBlur(img,5)
bilateral=cv2.bilateralFilter(img,9,75,75)
cv2.imshow("gaussian",gaussian)
cv2.imshow("median",median)
cv2.imshow("bilateral",bilateral)
cv2.imwrite("gaussian_blur.jpg",gaussian)
cv2.imwrite("median_blur.jpg",median)
cv2.imwrite("bilateral_blur.jpg",bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows