import cv2
video=cv2.VideoCapture(0)
while True:
    ret,frame=video.read()
    if not ret:
        break
    frame=cv2.resize(frame,(900,500))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Webcam",gray)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
video.release()
cv2.destroyAllWindows()