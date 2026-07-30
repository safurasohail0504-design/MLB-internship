from ultralytics import YOLO
model = YOLO("yolov8n.pt")
image_path = "Sample Input Images/image8.jpg"
results = model(image_path)
boxes = results[0].boxes
names = model.names
print("\nDetected Objects\n")
for box in boxes:
    class_id = int(box.cls[0])
    confidence = float(box.conf[0])
    print(f"Object : {names[class_id]}")
    print(f"Confidence : {confidence:.2f}")