from ultralytics import YOLO
model=YOLO("yolov8n.pt")
print("model loaded")
results=model.predict("C:/Users/User/Documents/GitHub/day_17/Helmet Detection.v7i.yolov8/test/images",
    save=True,show=True,conf=0.25)