from ultralytics import YOLO
model = YOLO("yolov8n.pt")
image_path = "Sample Input Images/image1.jpeg"
results = model(image_path)
results[0].save("Output Images and Videos/image1_output.jpg")