from ultralytics import YOLO
import cv2

model=YOLO("yolov8n.pt")

cap=cv2.VideoCapture("Sample Input Videos/video1.mp4")

width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps=int(cap.get(cv2.CAP_PROP_FPS))

writer=cv2.VideoWriter(
"Processed Output Videos/roi_video.mp4",
cv2.VideoWriter_fourcc(*"mp4v"),
fps,
(width,height)
)

line_x=380

while True:

    success,frame=cap.read()

    if not success:
        break

    results=model.track(
        frame,
        tracker="bytetrack.yaml",
        persist=True
    )

    frame=results[0].plot()

    cv2.line(
        frame,
        (line_x,0),
        (line_x,height),
        (0,255,255),
        4
    )

    cv2.putText(
        frame,
        "COUNTING LINE",
        (line_x-80,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,255),
        3
    )

    writer.write(frame)

writer.release()
cap.release()