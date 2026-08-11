from ultralytics import YOLO
model = YOLO("best.pt")
results = model.val(data="data.yaml",imgsz=640,split="val",plots=True)
print("\n MODEL EVALUATION :")
print(f"Precision: {results.box.mp:.4f}")
print(f"Recall: {results.box.mr:.4f}")
print(f"mAP@50: {results.box.map50:.4f}")
print(f"mAP@50-95: {results.box.map:.4f}")