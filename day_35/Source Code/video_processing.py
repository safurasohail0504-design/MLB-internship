import cv2
cap=cv2.VideoCapture("Sample Input Videos/video1.mp4")
fps=cap.get(cv2.CAP_PROP_FPS)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(cap.isOpened())
while True:
    success,frame=cap.read()
    if not success:
       break
print("frames",fps)
print("width",width)
print("height",height)
cap.release()