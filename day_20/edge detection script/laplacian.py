import cv2
import numpy as np
img=cv2.imread("output images/grayscale.jpg")
laplacian=cv2.Laplacian(img,cv2.CV_64F)
lap=cv2.convertScaleAbs(laplacian)
cv2.imshow("laplacian",lap)
cv2.imwrite("output images/laplacian.jpg",lap)
cv2.waitKey(0)
cv2.destroyAllWindows()