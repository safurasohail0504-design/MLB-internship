import cv2
binary = cv2.imread("Output Images/document1_binary.jpg")
adaptive = cv2.imread("Output Images/document1_adaptive.jpg")
otsu = cv2.imread("Output Images/document1_otsu.jpg")
compare = cv2.hconcat([binary,adaptive,otsu])
cv2.imwrite("Output Images/document1_compare.jpg",compare)