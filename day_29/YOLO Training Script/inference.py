from ultralytics import YOLO
import os
model = YOLO("runs/detect/train/weights/best.pt")
input_folder = "Sample Test Images"
output_folder = "Prediction Results"
os.makedirs(output_folder, exist_ok=True)
extensions = (".jpg", ".jpeg", ".png")
for image in os.listdir(input_folder):
    if image.lower().endswith(extensions):
        image_path = os.path.join(input_folder, image)
        results = model(image_path)
        output_path = os.path.join(output_folder, image)
        results[0].save(output_path)
        print(f"Saved: {output_path}")