from ultralytics import YOLO
model = YOLO("yolov8n.pt")
results = model.track(
    source="Sample Input Videos/video1.mp4",
    tracker="bytetrack.yaml",
    show=True,
    save=True
)