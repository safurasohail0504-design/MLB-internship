import cv2
import os
img=cv2.imread("sample images/img1.jpeg") 
rotate90=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
rotate180=cv2.rotate(img,cv2.ROTATE_180)
rotate270=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("rotated at 90",rotate90)
cv2.imshow("rotated at 180",rotate180)
cv2.imshow("rotated at 270",rotate90)
cv2.imwrite("rotated_TO_90.jpg",rotate90)
cv2.imwrite("rotated_TO_180.jpg",rotate180)
cv2.imwrite("rotated_TO_270.jpg",rotate270)
cv2.waitKey(0)
cv2.destroyAllWindows()