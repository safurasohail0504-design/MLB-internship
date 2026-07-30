from ultralytics import YOLO
model = YOLO("yolov8n.pt")
image_path = "Sample Input Images/image9.jpeg"
results = model(image_path)
boxes = results[0].boxes
names = model.names
for box in boxes:
    class_id = int(box.cls[0])
    confidence = float(box.conf[0])
    print(
        names[class_id],
        "Confidence:",
        round(confidence,2)
    )