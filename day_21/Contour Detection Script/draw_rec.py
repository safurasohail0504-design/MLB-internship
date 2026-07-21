import cv2
import pandas as pd
import numpy as np
img=cv2.imread("input images/sample_contour.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel=np.ones((3,3),np.uint8)
thresh=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    print("Contour", i + 1)
    print("Area:", area)
    print("Perimeter:", perimeter)
    if area >= 500:
        cv2.drawContours(img, [contour], -1, (0,255,0), 2)
    x,y,w,h=cv2.boundingRect(contour)
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow("Original",img)
cv2.imshow("Grayscale",gray)
cv2.imshow("Threshold",thresh)
cv2.imwrite("output images/bound_rec.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()