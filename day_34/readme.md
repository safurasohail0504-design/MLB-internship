# Day 34 – AI Smart Security Monitoring System

## Project Introduction

This project demonstrates an **AI Smart Security Monitoring System** using **YOLOv8**, **ByteTrack**, **OpenCV**, and **Streamlit**. The application allows users to upload CCTV or surveillance videos, automatically detect and track people, monitor entry and exit events using a virtual counting line and Region of Interest (ROI), calculate live occupancy and stay time, generate event logs, capture snapshots of detected people, preview the processed video, and download all generated results.

# Technologies Used

- Python
- Ultralytics YOLOv8
- ByteTrack
- OpenCV
- Streamlit
- Pandas
- NumPy
- CSV

# Folder Structure

```text
Day_34

├── app.py
├── output.mp4
├── requirements.txt
├── README.md
├── GitHub Repository Link.txt
└── Streamlit App URL.txt
```

# Features

The application can:

- Upload CCTV or surveillance videos
- Detect people using YOLOv8
- Track people using ByteTrack
- Select a custom Region of Interest (ROI)
- Adjust Confidence Threshold
- Adjust IoU Threshold
- Detect entry and exit events
- Calculate stay time for every tracked person
- Display live occupancy
- Display total entries and exits
- Display maximum occupancy
- Generate CSV event logs
- Capture snapshots automatically
- Preview processed video
- Download processed video
- Download event log (CSV)
- Download all captured snapshots

# Problem Statement

Monitoring surveillance footage manually is time-consuming and error-prone. Security personnel may miss important events such as unauthorized entry, occupancy limits, or movement patterns.

This application automates surveillance monitoring by detecting people, tracking them across video frames, identifying entry and exit events, calculating stay duration, recording all events, and generating downloadable reports.

# What is AI-Based Security Monitoring?

AI-Based Security Monitoring combines **Computer Vision**, **Deep Learning**, and **Object Tracking** to automatically analyze surveillance videos.

Instead of simply detecting people, the system understands movement patterns and generates meaningful events.

Examples include:

- Person entering a restricted area
- Person exiting a building
- Occupancy monitoring
- Visitor counting
- Security surveillance
- Stay time analysis

# Difference Between Object Detection and Object Tracking

## Object Detection

- Detects objects independently in every frame.
- Does not remember previously detected people.
- Cannot determine entry or exit events.

Example:

Frame 1 → Person

Frame 2 → Person

Frame 3 → Person

## Object Tracking

- Detects every person.
- Assigns a unique tracking ID.
- Tracks movement across multiple frames.
- Detects entry and exit events.
- Calculates stay time.
- Maintains occupancy statistics.

# How Entry and Exit Detection Works

A virtual counting line is placed at the center of the monitored area.

The system continuously tracks the center point of every detected person.

Movement direction determines the event:

- Left → Right = Entry
- Right → Left = Exit

Every detected person keeps the same tracking ID throughout the video, preventing duplicate counting.

# Region of Interest (ROI)

The application allows users to define a **Region of Interest (ROI)** before processing.

Only people detected inside the selected ROI are monitored.

Benefits include:

- Faster processing
- Fewer false detections
- Monitoring only important areas
- Improved counting accuracy

# Tracking Algorithm Used

This project uses **ByteTrack**, integrated with Ultralytics YOLOv8.

Reasons for using ByteTrack:

- High-speed tracking
- Stable tracking IDs
- Accurate multi-person tracking
- Prevents duplicate counting
- Suitable for real-time surveillance

# YOLO Model Used

The application uses the **YOLOv8 Nano (yolov8n.pt)** pre-trained model.

Only the **Person** class is monitored throughout the project.

# Mini Project

## AI Smart Security Monitoring System

The Streamlit application performs the following tasks:

- Upload surveillance videos
- Detect people
- Track multiple people
- Monitor entry and exit events
- Calculate stay time
- Display live occupancy
- Display maximum occupancy
- Generate event logs
- Capture snapshots
- Preview processed video
- Download processed video
- Download CSV report
- Download snapshots

# Dataset Used

The application was tested using surveillance-style videos containing people entering and leaving monitored areas.

Example scenarios include:

- Office entrances
- Shopping malls
- Building entrances
- Public hallways
- Indoor surveillance footage

# Event Logging

Every detected event is automatically stored inside **events.csv**.

Each record contains:

- Tracking ID
- Event Type
- Timestamp
- Stay Time

The event log can later be used for analytics and reporting.

# Stay Time Monitoring

Whenever a person enters the monitored area, the application records the entry time.

Once the same person exits, the total stay duration is calculated automatically.

This feature is useful for:

- Visitor management
- Employee attendance
- Occupancy analysis
- Security auditing

# Security Monitoring Results

The application successfully:

- Detected people using YOLOv8
- Tracked people using ByteTrack
- Maintained unique tracking IDs
- Detected entry events
- Detected exit events
- Calculated stay time
- Counted live occupancy
- Calculated maximum occupancy
- Generated CSV reports
- Saved person snapshots
- Produced processed surveillance videos

# Challenges Faced

During this project, I faced several challenges:

- Understanding ByteTrack integration
- Implementing ROI correctly
- Calculating stay time accurately
- Preventing duplicate counting
- Managing multiple tracking IDs
- Handling Streamlit UI updates
- Saving event logs automatically
- Processing long surveillance videos

# What I Learned

After completing this project, I learned how to:

- Build a complete AI surveillance application
- Detect people using YOLOv8
- Track multiple people using ByteTrack
- Implement Region of Interest (ROI)
- Monitor entry and exit events
- Calculate stay time
- Generate event logs
- Capture snapshots
- Build an interactive Streamlit dashboard
- Export AI-generated reports

# Possible Improvements

In future versions, I would like to add:

- Live webcam monitoring
- Polygon-based ROI
- Multiple monitoring zones
- Face recognition
- Fire and smoke detection
- Weapon detection
- Database integration
- Cloud storage
- Email alerts
- SMS notifications
- Real-time occupancy dashboard
- AI-based suspicious activity detection