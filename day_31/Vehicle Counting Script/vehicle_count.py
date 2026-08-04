from ultralytics import YOLO
import cv2
model = YOLO("yolov8n.pt")
video = "Sample Input Videos/video2.mp4"
cap = cv2.VideoCapture(video)
width = int(cap.get(3))
height = int(cap.get(4))
fps = int(cap.get(5))
out = cv2.VideoWriter(
    "Output Videos/vehicle_count2.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)
line_y = 300
count = 0
ids = []
while True:
    success, frame = cap.read()
    if not success:
        break
    results = model.track(frame, persist=True)
    boxes = results[0].boxes
    frame = results[0].plot()

    cv2.line(frame, (0,line_y), (width,line_y), (0,255,0), 3)

    if boxes.id is not None:

        for box, track_id in zip(boxes, boxes.id):

            x1, y1, x2, y2 = box.xyxy[0]

            center_y = int((y1+y2)/2)

            track_id = int(track_id)

            if center_y > line_y:

                if track_id not in ids:

                    ids.append(track_id)
                    count += 1

    cv2.putText(
        frame,
        "Count : " + str(count),
        (20,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,0,255),
        2
    )

    out.write(frame)

cap.release()
out.release()

print("Total Vehicles :", count)