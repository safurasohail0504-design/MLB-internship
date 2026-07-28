import cv2
import numpy as np
image=cv2.imread("Sample Image Pairs/pair1/book2.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
orb=cv2.ORB_create()
keypoints,descriptors=orb.detectAndCompute(gray,None)
output=cv2.drawKeypoints(image,keypoints,None,color=(0,255,0))
cv2.imwrite("Output Images/pair1_orb.jpg",output)