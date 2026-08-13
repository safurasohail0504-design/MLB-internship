from ultralytics import YOLO
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "runs", "shoe_detection_v1", "weights", "best.pt")
SOURCE_DIR = os.path.join(BASE_DIR, "test_images")
OUTPUT_DIR = os.path.join(BASE_DIR, "predictions")

model = YOLO(MODEL_PATH)

model.predict(
    source=SOURCE_DIR,
    imgsz=512,
    conf=0.25,
    save=True,
    project=OUTPUT_DIR,
    name="shoe_predictions"
)

print("Predictions saved to:", os.path.join(OUTPUT_DIR, "shoe_predictions"))