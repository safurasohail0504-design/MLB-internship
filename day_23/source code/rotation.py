import cv2
image=cv2.imread("Sample Input Images/object.jpg")
height,width,channel=image.shape
matrix=cv2.getRotationMatrix2D((width/2,height/2),45,1)
rotate=cv2.warpAffine(image,matrix,(width,height))
cv2.imshow("Rotation",rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()