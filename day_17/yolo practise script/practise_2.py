from ultralytics import YOLO
model = YOLO("yolov8n.pt")
print("model loaded")
results = model("C:/Users/User/Documents/GitHub/day_17/my_images",save=True,show=True)
