# Day 30 – Smart Object Tracking using YOLO

## Project Introduction

This project demonstrates a Smart Object Tracking System using YOLOv8, ByteTrack, and Streamlit. The application allows users to upload a video, automatically detect and track multiple objects, assign a unique tracking ID to each object, display confidence scores, count the total number of unique objects, preview the tracked video, and download the processed result.

# Technologies Used

* Python
* Ultralytics YOLOv8
* ByteTrack
* OpenCV
* NumPy
* Streamlit

# Folder Structure

```text
Day_30

├── Tracking Script
│   ├── video_tracking.py
│   ├── multiple_videos.py
│   ├── object_counter.py
│   ├── tracking_ids.py
│   └── save_tracking.py
│
├── Sample Input Videos
├── Output Videos
├── best.pt
├── app.py
├── requirements.txt
├── README.md
├── GitHub Repository Link.txt
└── Streamlit App URL.txt
```

# Features

The application can:
* Upload a video
* Detect and track multiple objects
* Assign unique IDs to each object
* Display confidence scores
* Count total unique tracked objects
* Preview the processed video
* Download the processed video

# What is Object Tracking?

Object Tracking is a Computer Vision technique that continuously follows the same object across multiple frames of a video.
Unlike object detection, tracking ensures that every detected object keeps the same identity (ID) while moving throughout the video.
Object Tracking is commonly used in:
* Traffic Monitoring
* Security Surveillance
* Sports Analytics
* Autonomous Vehicles
* Crowd Analysis
* Robotics

# Difference Between Object Detection and Object Tracking

### Object Detection

* Detects objects independently in every frame.
* Does not remember previously detected objects.
* No unique identity is assigned.

Example:

Frame 1 → Person
Frame 2 → Person
Frame 3 → Person

The model cannot determine whether it is the same person.

### Object Tracking

* Detects objects and follows them across frames.
* Assigns a unique tracking ID.
* Maintains the same ID while the object remains visible.

Example:

Person ID 1
Car ID 2
Helmet ID 3

Even when the objects move, their IDs remain consistent.

# Tracking Algorithm Used

This project uses **ByteTrack**, which is integrated into the **Ultralytics YOLOv8** framework.

Reasons for choosing ByteTrack:
* Fast tracking performance
* Stable object IDs
* Handles multiple objects efficiently
* Built directly into Ultralytics YOLO
* Suitable for real-time applications

# YOLO Model Used

The project uses the **custom Helmet Detection model (`best.pt`)** trained on Day 29.
The trained model was used for tracking helmets in videos.

# Coding Practice

Separate scripts were created to understand different stages of object tracking.

### video_tracking.py

* Track objects in a single video.
* Display tracking IDs.
* Save the tracked output.

### multiple_videos.py

* Run tracking on multiple videos.
* Automatically save processed videos.

### object_counter.py

* Count the total number of unique tracked objects.

### tracking_ids.py

* Display object IDs and confidence scores.

### save_tracking.py

* Save processed tracking videos

# Mini Project

## Smart Object Tracking System

The Streamlit application performs the following tasks:

* Upload a video
* Detect and track objects
* Display tracking IDs
* Display confidence scores
* Count unique tracked objects
* Preview the processed video
* Download the processed video

# Dataset Used

The model was tested on **5 short videos**, including:
* Traffic videos
* People walking
* Parking lot videos
* Road scenes
* Outdoor surveillance clips

# Tracking Results

The model successfully:
* Assigned unique IDs to detected objects.
* Maintained consistent IDs across video frames.
* Displayed confidence scores.
* Counted total unique tracked objects.
* Generated processed tracking videos.

# Challenges Faced

During this task, I faced several challenges:

* Understanding the difference between object detection and object tracking.
* Learning how tracking IDs remain consistent across frames.
* Processing videos efficiently using the YOLO tracking API.
* Managing video input and output formats.
* Counting only unique tracked objects.
* Deploying the Streamlit application successfully.

# What I Learned

After completing this task, I learned how to:

* Understand the fundamentals of Object Tracking.
* Track multiple objects using YOLOv8.
* Assign and maintain unique tracking IDs.
* Count unique tracked objects.
* Process videos using the YOLO tracking API.
* Build a Streamlit-based object tracking application.
* Organize a complete Computer Vision project professionally.

# Possible Improvements

In future versions, I would like to add:
* Live webcam object tracking
* Real-time tracking dashboard
* Object trajectory visualization
* Entry and exit counting
* Speed estimation
* Region-based counting
* Support for multiple custom-trained models
* Improved user interface