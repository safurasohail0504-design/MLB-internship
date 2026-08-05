from ultralytics import YOLO
import cv2
model=YOLO("yolov8n.pt")
cap=cv2.VideoCapture("Sample Input Videos/video1.mp4")
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps=int(cap.get(cv2.CAP_PROP_FPS))
writer=cv2.VideoWriter("Output Videos/output_video.mp4",cv2.VideoWriter_fourcc(*"mp4v"),fps,(width,height))
while True:
    success,frame=cap.read()
    if not success:
        break
    results=model.track(frame,tracker="bytetrack.yaml",persist=True)
    boxes=results[0].boxes
    people=0
    for box in boxes:
        cls=int(box.cls[0])
        if cls==0:
            people+=1
    annotated=results[0].plot()
    cv2.putText(annotated,"People: "+str(people),(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    writer.write(annotated)
cap.release()
writer.release()