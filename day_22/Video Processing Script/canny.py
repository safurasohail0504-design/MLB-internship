import cv2
video=cv2.VideoCapture("input video/sample_video.mp4")
while True:
    ret,frame=video.read()
    if not ret:
        break
    frame=cv2.resize(frame,(900,500))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canny=cv2.Canny(gray,100,200)
    cv2.imshow("Canny Video",canny)
    if cv2.waitKey(30)&0xFF==ord('q'):
        break
video.release()
cv2.destroyAllWindows()