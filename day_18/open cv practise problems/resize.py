import cv2
import os
img=cv2.imread("sample images/img1.jpeg")
new_img=cv2.resize(img,(500,300))
cv2.imshow("new",new_img)
cv2.imwrite("resize_img.jpg",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()