from ultralytics import YOLO
import cv2
import os
model = YOLO("yolov8n.pt")

# Input video
video_path = "Sample Input Images/video2.mp4"

# Output folder
output_folder = "Output Images and Videos"
os.makedirs(output_folder, exist_ok=True)

output_path = os.path.join(output_folder, "video2_output.mp4")

# Read video
cap = cv2.VideoCapture(video_path)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Save as MP4
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # YOLO prediction
    results = model(frame)

    # Draw boxes
    annotated_frame = results[0].plot()

    # Save frame
    writer.write(annotated_frame)

cap.release()
writer.release()

print("Video saved successfully!")
print(output_path)