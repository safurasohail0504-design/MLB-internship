# Day 33 – Intelligent Security Monitoring System using YOLOv8

## Project Introduction

This project demonstrates an **Intelligent Security Monitoring System** using **YOLOv8**, **ByteTrack**, **OpenCV**, and **Streamlit**. The application allows users to upload a surveillance video, automatically detect and track people, monitor entry and exit events using a virtual counting line, calculate live occupancy, save event logs into a CSV file, capture snapshots of new entries, preview the processed video, and download both the processed video and event log.

# Technologies Used
* Python
* Ultralytics YOLOv8
* ByteTrack
* OpenCV
* Streamlit
* CSV
# Folder Structure

```text
Day_33

├── Source Code
│   ├── detect_roi.py
│   ├── event_logger.py
│   ├── entry_exit.py
│
├── Sample Input Videos
├── Processed Output Videos
├── snapshots
├── events.csv
├── yolov8n.pt
├── app.py
├── requirements.txt
├── README.md
├── GitHub Repository Link.txt
└── Streamlit App URL.txt
```
# Features

The application can:
* Upload a surveillance video
* Detect and track people
* Draw a monitoring line (ROI)
* Detect entry and exit events
* Count current people inside the monitored area
* Display total entries and exits
* Display maximum occupancy
* Save all events into a CSV file
* Capture snapshots whenever a new person enters
* Preview the processed video
* Download the processed video
* Download the event log (CSV)

# Problem Statement

Security personnel often monitor surveillance cameras manually, making it difficult to accurately count people entering or leaving an area and maintain event records.
This application automates the monitoring process by detecting people, tracking them across video frames, recording entry and exit events, and generating structured reports.

# What is Event-Based Video Analytics?

Event-Based Video Analytics is a Computer Vision technique that continuously analyzes a video stream and generates meaningful events instead of simply detecting objects.

Examples include:
* Person entering a room
* Person leaving a room
* Vehicle entering a parking lot
* Crowd occupancy monitoring
* Security surveillance
Instead of only detecting people, the system also understands **what happened**.

# Difference Between Detection and Event Monitoring

## Object Detection
* Detects people in each frame.
* Does not remember previous detections.
* Cannot identify whether a person entered or exited.

Example:
Frame 1 → Person
Frame 2 → Person
Frame 3 → Person

## Event Monitoring
* Detects people.
* Tracks every person using a unique ID.
* Monitors movement across a monitoring line.
* Records entry and exit events.
* Stores event information for future analysis.


# How Entry and Exit Detection Works
A virtual counting line is placed in the monitored area.
The system continuously tracks each detected person's center point.
If the center moves:
* Left → Right = Entry
* Right → Left = Exit
Every tracked person keeps the same tracking ID throughout the video, preventing duplicate counting.

# Tracking Algorithm Used
This project uses **ByteTrack**, integrated with the Ultralytics YOLOv8 framework.
Reasons for using ByteTrack:
* Fast performance
* Stable tracking IDs
* Accurate multi-person tracking
* Prevents duplicate counting
* Suitable for surveillance applications

# YOLO Model Used
The application uses the **YOLOv8 Nano (yolov8n.pt)** pre-trained model for person detection.
Only the **Person** class is monitored throughout the project.

# Coding Practice
Separate scripts were created to understand different stages of the security monitoring pipeline.

### detect_roi.py
* Detect people
* Draw monitoring line
* Save processed video

### event_logger.py
* Detect entry events
* Generate event log (CSV)
* Save snapshots

### entry_exit.py
* Detect entries and exits
* Display live occupancy
* Display total entry and exit counts

# Mini Project

## Intelligent Security Monitoring System

The Streamlit application performs the following tasks:
* Upload a surveillance video
* Detect and track people
* Monitor entry and exit events
* Display live occupancy
* Display maximum occupancy
* Generate event logs
* Save snapshots
* Preview processed video
* Download processed video
* Download event log (CSV)

# Dataset Used
The application was tested using surveillance-style videos containing people entering and leaving monitored areas.
Example videos include:
* Office entrance
* Shopping mall entrance
* Building entrance
* Public hallway

# Event Logging

Every detected event is automatically stored inside **events.csv**.
Each record contains:
* Tracking ID
* Event Type (Entry / Exit)
* Timestamp
* Stay Time

This makes the system suitable for later analysis and reporting.

# Security Monitoring Results
The application successfully:
* Detected people using YOLOv8
* Tracked people using ByteTrack
* Maintained consistent tracking IDs
* Recorded entry events
* Recorded exit events
* Counted current occupancy
* Calculated maximum occupancy
* Generated CSV reports
* Captured entry snapshots
* Produced processed surveillance videos

# Challenges Faced
During this project, I faced several challenges:
* Understanding how event-based monitoring differs from simple object detection.
* Detecting entry and exit events accurately.
* Preventing duplicate event generation.
* Maintaining consistent tracking IDs.
* Managing CSV event logging.
* Handling different surveillance video angles.
* Building a complete Streamlit application.

# What I Learned
After completing this project, I learned how to:
* Build a complete video analytics pipeline.
* Detect and track multiple people.
* Implement entry and exit monitoring.
* Generate structured event logs.
* Save AI-generated reports.
* Capture event snapshots.
* Develop a production-style surveillance application using Streamlit.

# Possible Improvements
In future versions, I would like to add:
* Polygon-based Region of Interest (ROI)
* Multiple monitoring zones
* Live webcam monitoring
* Real-time email alerts
* Database integration
* Face recognition
* Intrusion detection
* Occupancy dashboard
* Cloud storage for event logs
* Real-time notification system