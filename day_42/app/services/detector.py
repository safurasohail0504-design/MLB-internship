from ultralytics import YOLO
from pathlib import Path
# Find best.pt inside day_41/models/
MODEL_PATH = Path(__file__).resolve().parents[2] / "models" / "best.pt"
# Load the YOLO model once when FastAPI starts
model = YOLO(str(MODEL_PATH))
def predict_image(image_path: str, confidence_threshold: float = 0.25):
    results = model(
        image_path,
        conf=confidence_threshold,
        verbose=False
    )
    detections = []
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = result.names[class_id]
            confidence = float(box.conf[0])
            bbox = box.xyxy[0].tolist()
            detections.append({
                "class": class_name,
                "confidence": round(confidence, 4),
                "bbox": [
                    round(float(x), 2)
                    for x in bbox
                ]
            })
    return detections