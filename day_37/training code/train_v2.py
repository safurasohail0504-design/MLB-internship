from ultralytics import YOLO
from pathlib import Path
BASE = Path(__file__).resolve().parent.parent
DATA = BASE / "improved_dataset" / "data.yaml"
V1 = BASE / "models" / "V1_best.pt"
RESULTS = BASE / "results"
print("========== V2 TRAINING ==========")
print(f"Dataset: {DATA}")
print(f"V1 Model: {V1}")
if not DATA.exists():
    raise FileNotFoundError(f"data.yaml not found: {DATA}")
if not V1.exists():
    raise FileNotFoundError(f"V1_best.pt not found: {V1}")
print("\nLoading V1 model...")
model = YOLO(str(V1))
print("V1 model loaded successfully.")
print("\nStarting V2 training...")
print("Training on improved helmet dataset.")
print("Epochs: 5")
results = model.train(
    data=str(DATA),
    epochs=5,
    imgsz=640,
    batch=8,
    workers=0,
    # Augmentation
    degrees=10,
    translate=0.1,
    scale=0.5,
    fliplr=0.5,
    flipud=0.0,
    # Color augmentation
    hsv_h=0.015,
    hsv_s=0.7,
    hsv_v=0.4,
    # Mosaic helps with small/difficult objects
    mosaic=0.5,
    # Training control
    patience=10,
    pretrained=True,
    optimizer="AdamW",
    # Keep best model
    save=True,
    plots=True,
    val=True,
    project=str(RESULTS),
    name="v2_training_correct",
    exist_ok=True
)
print("\n V2 TRAINING COMPLETED ")
best = RESULTS / "v2_training_correct" / "weights" / "best.pt"
last = RESULTS / "v2_training_correct" / "weights" / "last.pt"
print(f"Best V2 model: {best}")
print(f"Last V2 model: {last}")
if best.exists():
    print("\n✅ V2 best.pt created successfully.")
    print("Use this model for V1 vs V2 comparison.")
else:
    print("\n❌ best.pt was not created.")