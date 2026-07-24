import easyocr
import cv2
reader=easyocr.Reader(["en"])
image=cv2.imread("Sample Input Images/sample_doc.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,threshold=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
enhanced=cv2.convertScaleAbs(gray,alpha=1.5,beta=20)
original=reader.readtext(image)
gray_result=reader.readtext(gray)
threshold_result=reader.readtext(threshold)
enhanced_result=reader.readtext(enhanced)
result=reader.readtext(gray)
print("Original OCR")
for text in original:
    print(text[1])
print("Grayscale OCR")
for text in gray_result:
    print(text[1])
print("Threshold OCR")
for text in threshold_result:
    print(text[1])
print("Enhanced OCR")
for text in enhanced_result:
    print(text[1])