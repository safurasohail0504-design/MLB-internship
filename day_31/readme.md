# Day 31 – Smart Vehicle Counting using YOLO

## Project Introduction

This project demonstrates a **Smart Vehicle Counting System** using **YOLOv8**, **ByteTrack**, and **Streamlit**. The application allows users to upload a traffic video, automatically detect and track vehicles, count cars, buses, trucks, and motorcycles as they cross a counting line, display the live vehicle count on the video, preview the processed result, and download the output video.

# Technologies Used
* Python
* Ultralytics YOLOv8
* ByteTrack
* OpenCV
* NumPy
* Streamlit

# Folder Structure

```text
Day_31

├── Vehicle Counting Script
│   ├── tracking.py
│   ├── counting_line.py
│   ├── vehicle_count.py
│   └── save_video.py
│
├── Sample Input Videos
├── Output Videos
├── app.py
├── requirements.txt
├── README.md
├── GitHub Repository Link.txt
└── Streamlit App URL.txt
```
# Features

The application can:
* Upload a traffic video
* Detect vehicles
* Track vehicles with unique IDs
* Count cars, buses, trucks, and motorcycles
* Display live vehicle count
* Preview the processed video
* Download the processed video

# What is Vehicle Counting?

Vehicle Counting is a Computer Vision application that automatically counts vehicles passing through a road using object detection and tracking.
Instead of manually counting vehicles, AI systems detect every vehicle, follow it using a tracking ID, and increase the count whenever it crosses a predefined counting line.

Vehicle counting is widely used in:
* Smart Traffic Management
* Highway Monitoring
* Parking Management
* Toll Plaza Systems
* Smart Cities
* Traffic Analysis

# Difference Between Object Detection and Vehicle Counting

### Object Detection
* Detects vehicles in every frame.
* Draws bounding boxes.
* Does not count vehicles.
* Does not remember previous detections.

Example:

Frame 1 → Car
Frame 2 → Car
Frame 3 → Car

The same car is detected repeatedly.

### Vehicle Counting

* Detects vehicles.
* Tracks vehicles using unique IDs.
* Counts each vehicle only once.
* Uses a counting line to avoid duplicate counting.

Example:

```
Car ID 1 crosses line → Count = 1
Truck ID 2 crosses line → Count = 2
Bus ID 3 crosses line → Count = 3
```

# Counting Algorithm Used

The project uses **ByteTrack**, which is integrated into **Ultralytics YOLOv8**.
Reasons for using ByteTrack:
* Fast tracking
* Stable tracking IDs
* Prevents duplicate counting
* Handles multiple moving vehicles
* Suitable for traffic monitoring

# YOLO Model Used

This project uses the **YOLOv8 Nano (yolov8n.pt)** pre-trained model for vehicle detection and tracking.
Reasons:
* Lightweight
* Fast inference
* Suitable for CPU
* Supports built-in tracking

# Coding Practice

Separate scripts were created to understand every stage of vehicle counting.
### tracking.py

* Detect and track vehicles.
* Assign unique IDs.
* Save tracked video.

### counting_line.py

* Draw a counting line on the road.
* Display the line on every frame.

### vehicle_count.py

* Count vehicles crossing the counting line.
* Display live vehicle count.

# Mini Project

## Smart Vehicle Counting System

The Streamlit application performs the following tasks:
* Upload a traffic video
* Detect vehicles
* Track vehicles
* Count cars, buses, trucks, and motorcycles
* Display live vehicle count
* Preview the processed video
* Download the processed video

# Dataset Used

The application was tested on **3 traffic videos**, including:
* Highway traffic
* Road traffic
* Multiple vehicles moving in different directions

# Vehicle Classes Counted

The application counts:

* Car
* Bus
* Truck
* Motorcycle

Each vehicle is counted only once when it crosses the counting line.

# How Vehicle Counting Works

1. Upload a traffic video.
2. YOLO detects vehicles in every frame.
3. ByteTrack assigns a unique ID to every vehicle.
4. A counting line is drawn on the road.
5. Whenever a tracked vehicle crosses the line, the count increases.
6. The total count is displayed live on the video.
7. The processed video is saved.

# Challenges Faced

During this task, I faced several challenges:

* Understanding the difference between object tracking and vehicle counting.
* Learning how counting lines prevent duplicate counting.
* Keeping tracking IDs consistent while vehicles move.
* Processing videos efficiently using YOLO tracking.
* Saving processed videos correctly.
* Deploying the Streamlit application.

# What I Learned

After completing this task, I learned how to:

* Understand vehicle counting concepts.
* Detect and track vehicles using YOLOv8.
* Assign unique tracking IDs.
* Draw counting lines.
* Count vehicles crossing a specific region.
* Build a Streamlit-based vehicle counting application.
* Organize a Computer Vision project professionally.

# Possible Improvements

In future versions, I would like to add:

* Bidirectional vehicle counting
* Vehicle speed estimation
* Lane-wise vehicle counting
* Traffic density analysis
* Live webcam traffic monitoring
* Automatic report generation
* Vehicle type statistics dashboard
* Better user interface