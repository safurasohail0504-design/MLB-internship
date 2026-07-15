import cv2
import os
img=cv2.imread("C:/Users/User/Documents/GitHub/day_18/sample images/img1.jpeg")
print(img)
cv2.imshow("ouput images",img)
height,width,channel=img.shape
print("height:",height)
print("width:",width)
print("channel:",channel)
size=os.path.getsize("C:/Users/User/Documents/GitHub/day_18/sample images/img1.jpeg")
print("file size:",size,"bytes")
cv2.waitKey(0)
cv2.destroyAllWindows()