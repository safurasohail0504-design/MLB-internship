import cv2
import numpy as np
img=cv2.imread("input images/sample_edge.jpg")
blur=cv2.GaussianBlur(img,(9,9),0)
cv2.imshow("guassian_blur",blur)
cv2.imwrite("output images/guassian_blur.jpg",blur)