import cv2
import numpy as np
image=cv2.imread("Sample Image Pairs/pair1/book1.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)
corners=cv2.cornerHarris(gray,2,3,0.04)
corners=cv2.dilate(corners,None)
image[corners>0.01*corners.max()]=[0,0,255]
cv2.imwrite("Output Images/pair1_harris.jpg",image)