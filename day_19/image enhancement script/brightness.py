import cv2
import numpy as np
img=cv2.imread("C:/Users/User/Documents/GitHub/day_19/sample_translation.jpeg")
bright=cv2.convertScaleAbs(img,beta=50)
dark=cv2.convertScaleAbs(img,beta=-50)
cv2.imshow("increase_rightness",bright)
cv2.imshow("decrease_brightness",dark)
cv2.imwrite("bright.jpg",bright)
cv2.imwrite("dark.jpg",dark)
cv2.waitKey(0)
cv2.destroyAllWindows