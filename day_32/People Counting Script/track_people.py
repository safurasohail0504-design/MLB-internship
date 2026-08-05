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
    annotated=results[0].plot()
    writer.write(annotated)
cap.release()
writer.release()