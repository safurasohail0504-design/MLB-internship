# Day 28 – Smart Object Detection using YOLO

## Project Introduction

This project demonstrates a simple **Smart Object Detection Application** using **YOLOv8** and **Streamlit**. The application allows users to upload an image, automatically detect multiple objects, draw bounding boxes around detected objects, display their class names along with confidence scores, preview the detection result, and download the processed image.

The project was developed as part of the **MLB AI Internship Day 28** task and focuses on understanding modern object detection using a pre-trained YOLO model.

# Technologies Used

* Python
* Ultralytics YOLOv8
* OpenCV
* NumPy
* Pillow
* Streamlit

# Folder Structure

```
Day_28

├── YOLO Practice Script
│   ├── image_detection.py
│   ├── multiple_images.py
│   ├── confidence_scores.py
│   ├── save_results.py
│   └── video_detection.py
│
├── Sample Input Images
├── Output Images and Videos
├── app.py
├── requirements.txt
├── README.md
├── GitHub Repository Link.txt
└── ngrok Public URL.txt
```

# Features

The application can:

* Upload an image
* Detect multiple objects using YOLOv8
* Draw bounding boxes around detected objects
* Display detected class names
* Display confidence scores
* Preview the processed image
* Download the processed image


# What is Object Detection?

Object Detection is a Computer Vision technique that identifies one or more objects present in an image and also determines their exact locations by drawing bounding boxes around them.

Unlike simple image recognition, Object Detection answers two questions:

* **What object is present?**
* **Where is the object located?**

Object Detection is widely used in:

* Self-driving vehicles
* Security surveillance
* Traffic monitoring
* Retail analytics
* Medical imaging
* Robotics

---

# How YOLO is Different from Image Classification

### Image Classification

* Predicts only the category of an image.
* Produces one output label.
* Does not identify object locations.

Example:

```
Image → Dog
```

---

### YOLO (You Only Look Once)

* Detects multiple objects in a single image.
* Draws bounding boxes around each detected object.
* Predicts class names and confidence scores simultaneously.
* Performs detection in a single forward pass, making it very fast.

Example:

```
Person (98%)
Car (95%)
Traffic Light (89%)
```

---

# YOLO Model Used

For this project, the **YOLOv8 Nano (yolov8n.pt)** pre-trained model from Ultralytics was used.

Reasons for choosing YOLOv8 Nano:

* Lightweight
* Fast inference
* Suitable for beginners
* Works efficiently on CPU
* Good balance between speed and accuracy

---

# Coding Practice

Separate scripts were created to understand YOLO inference step by step.

### image_detection.py

* Detect objects in a single image.
* Save the detected output.

### multiple_images.py

* Detect objects on multiple images.
* Automatically save all results.

### confidence_scores.py

* Display detected class names.
* Print confidence scores for every detected object.

### save_results.py

* Save processed detection results.

### video_detection.py

* Perform object detection on videos using YOLO.

---

# Mini Project

## Smart Object Detection Application

The Streamlit application performs the following tasks:

* Upload an image
* Detect objects automatically
* Display the original image
* Display the detected image
* Show detected object names
* Show confidence scores
* Download the processed image

---

# Dataset Used

The YOLO model was tested on **10 different images**, including:

* Cars
* People
* Buses
* Bicycles
* Dogs
* Cats
* Buildings
* Traffic scenes
* Street images
* Everyday outdoor objects

---

# Objects Detected

During testing, the application successfully detected objects such as:

* Person
* Car
* Bus
* Bicycle
* Motorcycle
* Truck
* Dog
* Cat
* Chair
* Bottle
* Laptop
* Cell Phone
* Traffic Light
* Bench

The detected objects varied depending on the uploaded image.

---

# How to Run the Project

### Clone Repository

```bash
git clone <repository_link>
```

### Open Project Folder

```bash
cd Day_28
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Coding Practice Scripts

```bash
python "YOLO Practice Script/image_detection.py"

python "YOLO Practice Script/multiple_images.py"

python "YOLO Practice Script/confidence_scores.py"

python "YOLO Practice Script/save_results.py"

python "YOLO Practice Script/video_detection.py"
```

### Run Streamlit Application

```bash
streamlit run app.py
```

---

# Challenges Faced

During this task, I faced several challenges:

* Understanding the difference between image classification and object detection.
* Learning how YOLO predicts multiple objects in a single image.
* Organizing YOLO outputs properly.
* Saving processed images correctly.
* Configuring Streamlit for deployment.
* Setting up ngrok and keeping the public URL active.
* Troubleshooting deployment and temporary URL issues.

---

# What I Learned

After completing this task, I learned how to:

* Understand the fundamentals of Object Detection.
* Use a pre-trained YOLOv8 model.
* Detect multiple objects from images.
* Interpret class labels and confidence scores.
* Draw bounding boxes around detected objects.
* Build a Streamlit-based object detection application.
* Organize a Computer Vision project professionally.

---

# Possible Improvements

In future versions, I would like to add:

* Live webcam object detection
* Real-time video detection
* Confidence threshold adjustment
* Support for custom-trained YOLO models
* Detection statistics dashboard
* Multiple image upload support
* Improved user interface