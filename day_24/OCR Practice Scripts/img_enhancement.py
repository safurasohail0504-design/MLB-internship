import easyocr
import cv2
reader=easyocr.Reader(["en"])
image=cv2.imread("Sample Input Images/sample_doc.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
enhanced=cv2.convertScaleAbs(gray,alpha=1.5,beta=20)
result=reader.readtext(gray)
for detection in result:
    print(detection[1])