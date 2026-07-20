import cv2
import numpy as np
img=cv2.imread("input images/sample_edge.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscaled",gray)
cv2.imwrite("output images/grayscale.jpg",gray)