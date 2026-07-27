import easyocr
import cv2
import os
reader = easyocr.Reader(["en"])
image = cv2.imread("Sample Input Images/invoice.jpg")
result = reader.readtext(image)
text = ""
for item in result:
    text += item[1] + "\n"
filename = os.path.splitext(os.path.basename("Sample Input Images/invoice.jpg"))[0]
output_path = f"Sample Output Results/{filename}.txt"
with open(output_path, "w", encoding="utf-8") as file:
    file.write(text)