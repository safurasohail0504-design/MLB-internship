import easyocr
import cv2
reader = easyocr.Reader(["en"])
image = cv2.imread("Sample Input Images/sample_processing.jpg")
result = reader.readtext(image)
print("Extracted Text")
for item in result:
    print(item[1])