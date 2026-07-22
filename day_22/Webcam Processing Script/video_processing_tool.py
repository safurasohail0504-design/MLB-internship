import cv2
cv2.VideoCapture(0)
#video=cv2.VideoCapture("input video/sample_project.mp4")
video=cv2.VideoCapture(0)  #to test your application using your webcam
fps=video.get(cv2.CAP_PROP_FPS)
fourcc=cv2.VideoWriter_fourcc(*"mp4v")
output=cv2.VideoWriter("Processed Output Video/processed_video.mp4",fourcc,fps,(900,500),False)
if not output.isOpened():
    print("VideoWriter failed")
while True:
    ret,frame=video.read()
    if not ret:
        break
    frame=cv2.resize(frame,(900,500))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur,100,200)
    cv2.imshow("Original Video",frame)
    cv2.imshow("Processed Video",canny)
    output.write(canny)
    if cv2.waitKey(30)&0xFF==ord('q'):
        break
video.release()
output.release()
cv2.destroyAllWindows() 