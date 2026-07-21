import cv2
import numpy as np
images=[
"img1.png",
"img2.png",
"img3.png",
"img4.png",
"img5.png",
"img6.png",
"img7.png",
"img8.png",
"img9.png",
"img10.png"
]
for image in images:
    img=cv2.imread("input images/"+image)
    if img is None:
        print(image,"Not Found")
        continue
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)
    contours,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area=cv2.contourArea(contour)
        if area<500:
            continue
        perimeter=cv2.arcLength(contour,True)
        approx=cv2.approxPolyDP(contour,0.04*perimeter,True)
        vertices=len(approx)
        x,y,w,h=cv2.boundingRect(approx)
        ratio=w/float(h)
        if vertices==3:
            shape="Triangle"
        elif vertices==4:
            if 0.95<=ratio<=1.05:
                shape="Square"
            else:
                shape="Rectangle"
        elif vertices==5:
            shape="Pentagon"
        elif vertices==6:
            shape="Hexagon"
        else:
            circularity=4*3.14*area/(perimeter*perimeter)
            if circularity>0.80:
                shape="Circle"
            else:
                shape="Polygon"
        cv2.drawContours(img,[approx],-1,(0,255,0),2)
        cv2.putText(img,shape,(x,y-25),
        cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,0),2)
        cv2.putText(img,"A:"+str(int(area)),(x,y),
        cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
        cv2.putText(img,"P:"+str(int(perimeter)),(x,y+20),
        cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
    cv2.imwrite("output images/output_"+image,img)
    cv2.imshow(image,img)
cv2.waitKey(0)
cv2.destroyAllWindows()