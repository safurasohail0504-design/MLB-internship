import easyocr
import cv2
reader=easyocr.Reader(["en"])
image=cv2.imread("Sample Input Images/invoice.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
result=reader.readtext(gray)
for detection in result:
    print(detection[1])