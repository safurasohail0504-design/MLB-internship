from ultralytics import YOLO
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "runs", "shoe_detection_v1", "weights", "best.pt")
DATA_YAML = os.path.join(BASE_DIR, "yolo_dataset", "data.yaml")

model = YOLO(MODEL_PATH)

results = model.val(
    data=DATA_YAML,
    imgsz=512,
    split="test",
    plots=True
)

print("Precision:", results.box.mp)
print("mAP50:", results.box.map50)
print("mAP50-95:", results.box.map)