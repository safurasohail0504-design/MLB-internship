from ultralytics import YOLO
import torch
import os

print("GPU Available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_YAML = os.path.join(BASE_DIR, "yolo_dataset", "data.yaml")
RUNS_DIR = os.path.join(BASE_DIR, "runs")

model = YOLO("yolov8n.pt")

results = model.train(
    data=DATA_YAML,
    epochs=10,
    imgsz=512,
    batch=16,
    project=RUNS_DIR,
    name="shoe_detection_v1",
    patience=5,
    plots=True
)

print("Training completed.")
print("Results saved in:", os.path.join(RUNS_DIR, "shoe_detection_v1"))