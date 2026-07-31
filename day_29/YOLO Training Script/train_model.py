from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model.train(data="Helmet_Dataset/data.yaml",epochs=20,imgsz=640,batch=8)