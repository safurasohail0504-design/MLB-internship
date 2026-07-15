import cv2
import numpy as np
img=cv2.imread("sample images/img1.jpeg")
cv2.rectangle(img,(50,50),(250,250),(0,255,0),3)
cv2.circle(img,(400,200),60,(255,0,0),3)
cv2.line(img,(20,600),(500,600),(0,0,255),4)
points=np.array([[300,700],[450,850],[150,850]], np.int32)
cv2.polylines(img,[points],True,(255,255,0),3)
cv2.imshow("shapes",img)
cv2.imwrite("shapes.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()