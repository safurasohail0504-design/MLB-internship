import cv2
img=cv2.imread("C:/Users/User/Documents/GitHub/day_19/sample_translation.jpeg")
height,width,chanel=img.shape
up=cv2.resize(img,None,fx=1.5,fy=1.5)
down=cv2.resize(img,None,fx=0.7,fy=0.7)
cv2.imshow("original",img)
cv2.imshow("scaled_Up",up)
cv2.imshow("scaled_down",down)
cv2.imwrite("scaled_up.jpg",up)
cv2.imwrite("scaled_down.jpg",down)
cv2.waitKey(0)
cv2.destroyAllWindows