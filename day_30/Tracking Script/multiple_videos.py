from ultralytics import YOLO
import os
model = YOLO("yolov8n.pt")
folder = "Sample Input Videos"
for video in os.listdir(folder):
    path = os.path.join(folder, video)
    model.track(
        source=path,
        tracker="bytetrack.yaml",
        save=True
    )
print("All Videos Completed")