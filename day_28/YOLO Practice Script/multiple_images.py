import os
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
input_folder = "Sample Input Images"
output_folder = "Output Images and Videos"
os.makedirs(output_folder, exist_ok=True)
for file in os.listdir(input_folder):
    if file.endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(input_folder, file)
        results = model(image_path)
        save_path = os.path.join(output_folder, file)
        results[0].save(save_path)
        print(file, "processed")