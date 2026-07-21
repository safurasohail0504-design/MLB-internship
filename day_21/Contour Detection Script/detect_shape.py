import cv2
import numpy as np

img=cv2.imread("input images/shape.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:

    area=cv2.contourArea(contour)

    if area<300:
        continue

    perimeter=cv2.arcLength(contour,True)

    approx=cv2.approxPolyDP(contour,0.04*perimeter,True)

    x,y,w,h=cv2.boundingRect(approx)

    shape="Unknown"

    if len(approx)==3:
        shape="Triangle"

    elif len(approx)==4:

        ratio=w/float(h)

        if 0.95<=ratio<=1.05:
            shape="Square"
        else:
            shape="Rectangle"

    elif len(approx)>=8:
        shape="Circle"

    else:
        shape="Polygon"

    cv2.drawContours(img,[approx],-1,(0,255,0),2)
    cv2.putText(img,shape,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)

cv2.imwrite("output images/detect_shape.jpg",img)

cv2.imshow("Threshold",thresh)
cv2.imshow("Detected Shapes",img)

cv2.waitKey(0)
cv2.destroyAllWindows()