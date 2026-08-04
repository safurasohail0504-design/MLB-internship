from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

video = "Sample Input Videos/video2.mp4"

cap = cv2.VideoCapture(video)

width = int(cap.get(3))
height = int(cap.get(4))
fps = int(cap.get(5))

out = cv2.VideoWriter(
    "Output Videos/counting_line2.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)

line_y = 300

while True:

    success, frame = cap.read()

    if not success:
        break

    results = model.track(frame, persist=True)

    frame = results[0].plot()

    cv2.line(frame, (0, line_y), (width, line_y), (0,255,0), 3)

    out.write(frame)

cap.release()
out.release()

print("Line Added Successfully")