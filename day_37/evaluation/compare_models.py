from ultralytics import YOLO
from pathlib import Path
V1_MODEL = Path("models/V1_best.pt")
V2_MODEL = Path("models/V2_best.pt")
DATA = r"C:\Users\User\Documents\GitHub\day_29\Helmet_Dataset\data.yaml"
def evaluate(model_path, name):
    print(f"\n {name}")
    model = YOLO(str(model_path))
    results = model.val(
        data=DATA,
        imgsz=640,
        split="val",
        plots=True,
        verbose=True
    )
    metrics = {
        "Precision": results.box.mp,
        "Recall": results.box.mr,
        "mAP50": results.box.map50,
        "mAP50-95": results.box.map,
    }
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")
    return metrics
v1 = evaluate(V1_MODEL, "V1 MODEL")
v2 = evaluate(V2_MODEL, "V2 MODEL")
print("\nV1 vs V2")
print(f"{'Metric':<15} {'V1':>10} {'V2':>10}")
print("-" * 37)
for metric in v1:
    print(f"{metric:<15} {v1[metric]:>10.4f} {v2[metric]:>10.4f}")