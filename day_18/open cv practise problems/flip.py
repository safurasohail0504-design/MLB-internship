import cv2
import os
img=cv2.imread("sample images/img1.jpeg") 
horizontal=cv2.flip(img,1)
vertical=cv2.flip(img,0)
both=cv2.flip(img,-1)

cv2.imshow("flip_TO_horizontal",horizontal)
cv2.imshow("flip_TO_horizon",vertical)
cv2.imshow("flip_TO_both",both)

cv2.imwrite("flip_TO_horizontal.jpg",horizontal)
cv2.imwrite("flip_TO_vertical.jpg",vertical)
cv2.imwrite("flip_TO_both.jpg",both)
cv2.waitKey(0)
cv2.destroyAllWindows()