from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model.track(
    source="Sample Input Videos/video1.mp4",
    save=True,
    tracker="bytetrack.yaml"
)
print("Video Saved")