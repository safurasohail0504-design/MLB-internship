from ultralytics import YOLO
model = YOLO("yolov8n.pt")
unique_ids = set()
results = model.track(
    source="Sample Input Videos/video1.mp4",
    tracker="bytetrack.yaml",
    stream=True
)
for r in results:
    if r.boxes.id is not None:
        ids = r.boxes.id.cpu().numpy()
        for i in ids:
            unique_ids.add(int(i))
print("Unique Objects:", len(unique_ids))