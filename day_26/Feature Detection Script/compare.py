import cv2
harris=cv2.imread("Output Images/pair1_harris.jpg")
orb=cv2.imread("Output Images/pair1_orb.jpg")
harris=cv2.resize(harris,(500, 400))
orb=cv2.resize(orb,(500,400))
compare=cv2.hconcat([harris,orb])
cv2.imwrite("Output Images/pair1_compare.jpg",compare)