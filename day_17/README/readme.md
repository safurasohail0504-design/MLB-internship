# Day 17 - Object Detection using YOLO

## Project Overview:

In this project, I learned the basics of Object Detection using the YOLOv8 pre-trained model. I explored how YOLO detects multiple objects in an image by predicting their class labels, confidence scores, and bounding boxes without training a custom model.

## What is Object Detection?

Object Detection is a Computer Vision technique that identifies **what objects are present in an image** and **where they are located**. It draws bounding boxes around detected objects and assigns a class label along with a confidence score.

## How is it Different from Image Classification?

Image Classification Predicts one label for the entire image.Object Detection Detects multiple objects in a single image.
Image Classification Does not provide object locations.
Object Detection Provides object locations using bounding boxes.
Example of Image Classification: "This is a cat." 
Example of Object Detection: Detects a cat, dog, and person with separate boxes.

## What is YOLO?

YOLO (You Only Look Once) is a fast and efficient real-time object detection algorithm. It processes an entire image in a single pass and predicts:

- Bounding Boxes
- Class Labels
- Confidence Scores

Because of its speed and accuracy, YOLO is widely used in applications such as autonomous vehicles, surveillance systems, robotics, and traffic monitoring.

## Dataset Used

- Helmet Detection Dataset (Roboflow Universe)
- Images were used for inference with the pre-trained YOLOv8 Nano model.

## Objects Detected

The model detected:

- Helmet

For each detected object, YOLO displayed:

- Bounding Box
- Class Label
- Confidence Score

## Observations

- The YOLOv8 Nano model successfully detected helmets in most images.
- Detection performance was better on clear and well-lit images.
- Confidence scores were generally higher when the object was fully visible.
- Images with partial occlusion or lower quality resulted in lower confidence scores.
- The pre-trained model performed inference without requiring additional training.

## Technologies Used

- Python
- Ultralytics YOLOv8
- OpenCV
- VS Code

## Learning Outcomes

Through this project, I learned:

- Fundamentals of Object Detection
- Difference between Image Classification and Object Detection
- How to use a pre-trained YOLO model
- How YOLO performs inference on images
- How to interpret bounding boxes, class labels, and confidence scores
- How to visualize and save object detection results