import cv2

image = cv2.imread("Sample Input Images/document1.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite(
    "Output Images/document1_gray.jpg",
    gray
)

print("Grayscale image saved successfully.")