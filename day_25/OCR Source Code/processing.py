import cv2
import os
image = cv2.imread("Sample Input Images/id card.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)
threshold = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)[1]
filename = os.path.splitext(os.path.basename("Sample Input Images/id card.jpg"))[0]
output_folder = "Sample Output Results"
cv2.imwrite(f"{output_folder}/{filename}_gray.jpg", gray)
cv2.imwrite(f"{output_folder}/{filename}_blur.jpg", blur)
cv2.imwrite(f"{output_folder}/{filename}_threshold.jpg", threshold)