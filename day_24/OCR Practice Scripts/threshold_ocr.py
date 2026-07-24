import easyocr
import cv2
import numpy as np
reader=easyocr.Reader(["en"])
image=cv2.imread("Sample Input Images/id card.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,threshold=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
result=reader.readtext(threshold)
for detection in result:
    print(detection[1])