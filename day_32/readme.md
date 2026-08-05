# Day 32 – Smart People Counting System using YOLO

## Project Introduction

This project demonstrates a Smart People Counting System using YOLOv8, ByteTrack, OpenCV, and Streamlit. The application allows users to upload an image or video, automatically detect and track people, count the total number of people visible, display entry and exit counts, show the maximum number of people detected during the video, preview the processed output, and download the final result.

# Technologies Used

* Python
* Ultralytics YOLOv8
* ByteTrack
* OpenCV
* NumPy
* Streamlit

# Folder Structure

```text
Day_32

├── People Counting Script
│   ├── detect_people.py
│   ├── people_counter.py
│   ├── track_people.py
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
* Upload an image or video
* Detect people using YOLOv8
* Track every detected person
* Assign a unique tracking ID to each person
* Display confidence scores
* Display live people count
* Display entry count
* Display exit count
* Display maximum people detected
* Save processed output
* Download processed output

# What is People Counting?

People Counting is a Computer Vision application that automatically detects and counts the number of people present in an image or video.
It is widely used in:
* Shopping Malls
* Airports
* Offices
* Retail Stores
* Smart Cities
* Public Events
* Security Systems

# Difference Between People Detection and People Counting

## People Detection

* Detects every person individually.
* Draws a bounding box around each person.
* Does not calculate the total number of people.

Example:
Person
Person
Person

## People Counting

* Detects people.
* Counts the total number of people.
* Can monitor live occupancy.
* Can calculate entry and exit counts.

Example:
People = 12
Entry = 5
Exit = 3

# Difference Between Counting and Tracking

## Counting

* Counts how many people are visible.
* Same person may be counted again if not tracked.

## Tracking

* Assigns a unique ID to every detected person.
* Maintains the same ID while the person remains visible.
* Prevents duplicate counting.

Example
ID 1
ID 2
ID 3

# Tracking Algorithm Used

This project uses **ByteTrack** integrated with **YOLOv8**.
Reasons for choosing ByteTrack:
* Fast tracking
* Stable tracking IDs
* Prevents duplicate counting
* Works well for multiple people
* Suitable for real-time applications

# YOLO Model Used

The project uses the pretrained **YOLOv8 Nano (yolov8n.pt)** model provided by Ultralytics.
The model detects people and other COCO dataset classes.

# Coding Practice

Separate scripts were created to understand each stage of people counting.

## detect_people.py

* Detect people using YOLO.
* Draw bounding boxes.
* Display confidence scores.
* Save processed video.

## people_counter.py

* Count total people visible in every frame.
* Display live people count.
* Save processed output.

## track_people.py

* Track people using ByteTrack.
* Assign unique tracking IDs.
* Keep IDs consistent while people move.
* Save processed output.

# Mini Project

## Smart People Counting System

The Streamlit application performs the following tasks:
* Upload image or video
* Detect people
* Track people
* Display confidence scores
* Display live people count
* Display entry count
* Display exit count
* Display maximum people detected
* Save processed output
* Download processed output

# Dataset Used

The application was tested on multiple public traffic and crowd videos including:
* Shopping Mall
* Public Street
* Campus Walkway
* Office Entrance
* Busy Crowd Scene

Videos were downloaded from:
* Pexels

# Counting Method

The project uses a horizontal counting line.
When a tracked person crosses the line:
* Top → Bottom = Entry
* Bottom → Top = Exit
Tracking IDs ensure that the same person is counted only once.
# Results

The application successfully:
* Detected people.
* Assigned stable tracking IDs.
* Counted live people.
* Counted entries.
* Counted exits.
* Recorded maximum occupancy.
* Generated processed output videos.

# Challenges Faced

During this task, I faced several challenges:
* Detecting people in crowded scenes.
* People overlapping each other.
* Maintaining consistent tracking IDs.
* Preventing duplicate counting.
* Understanding entry and exit counting logic.
* Deploying the Streamlit application successfully.

# What I Learned

After completing this task, I learned how to:
* Detect people using YOLOv8.
* Count people in images and videos.
* Track people using ByteTrack.
* Assign consistent tracking IDs.
* Calculate entry and exit counts.
* Monitor maximum occupancy.
* Build a Streamlit-based people counting application.
* Organize a complete Computer Vision project.

# Possible Improvements

In future versions, I would like to add:
* Live webcam people counting
* Region-based counting
* Crowd density estimation
* Multiple counting zones
* Face blurring for privacy
* Real-time dashboard