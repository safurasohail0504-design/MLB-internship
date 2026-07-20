import cv2
import numpy as np
img=cv2.imread("output images/grayscale.jpg")
sobel_x=cv2.Sobel(img,cv2.CV_64F,1,0,3)
sobel_y=cv2.Sobel(img,cv2.CV_64F,0,1,3)
sobel_x=cv2.convertScaleAbs(sobel_x)
sobel_y=cv2.convertScaleAbs(sobel_y)
cv2.imshow("sobel_x",sobel_x)
cv2.imshow("sobel_y",sobel_y)
cv2.imwrite("output images/sobel_x.jpg",sobel_x)
cv2.imwrite("output images/sobel_y.jpg",sobel_y)