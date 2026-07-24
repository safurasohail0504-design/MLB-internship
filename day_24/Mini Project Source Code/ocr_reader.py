import easyocr
import cv2
import matplotlib.pyplot as plt
reader=easyocr.Reader(["en"])
image_name=input("Enter image name with extension:")
image=cv2.imread("Sample Input Images/" + image_name)
result = reader.readtext(image)
text = ""
for detection in result:
    text=text+detection[1] + "\n"
print(text)
file_name=image_name.split(".")[0]
file=open("Extracted Text Files/" +file_name+".txt","w")
file.write(text)
file.close()
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")
plt.show()