import easyocr
reader=easyocr.Reader(["en"])
image ="Sample Input Images/sample_doc.jpg"
result=reader.readtext(image)
for detection in result:
    print(detection[1])