from ultralytics import YOLO
model = YOLO("runs/detect/train/weights/best.pt")
metrics = model.val()
print("Evaluation Results")
print(f"mAP50 : {metrics.box.map50:.3f}")
print(f"mAP50-95 : {metrics.box.map:.3f}")
print(f"Precision : {metrics.box.mp:.3f}")
print(f"Recall : {metrics.box.mr:.3f}")