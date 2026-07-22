# Day 22 – Video Processing with OpenCV

## Overview

In this task, I learned how to process videos using OpenCV by reading videos frame by frame, applying different image processing techniques to each frame, and saving the processed output as a new video. I also learned how to capture live video from a webcam and process it in real time.

## Technologies Used
* Python
* OpenCV
* NumPy

## Project Structure
Day_22
│
├── Video Processing Script
├── Webcam Processing Script
├── Challenge Task
├── Input Video
├── Processed Output Video
├── README

# Coding Practice Completed

## Reading and Displaying Video
* Loaded a video using OpenCV.
* Displayed the video frame by frame.
* Learned how videos are processed one frame at a time.

## Video Properties
* Printed the video's FPS (Frames Per Second).
* Retrieved the video width and height.
* Retrieved the total number of frames.

## Grayscale Conversion
* Converted every frame of the video to grayscale.
* Displayed the grayscale video in real time.

## Canny Edge Detection
* Applied Gaussian Blur to reduce image noise.
* Applied Canny Edge Detection to every frame.
* Displayed the edge-detected video.

## Saving Processed Video
* Created a VideoWriter object.
* Saved the processed video into the output folder.
* Maintained the original frame size and FPS while saving.

## Webcam Processing
* Captured live video from the webcam.
* Processed every frame in real time.
* Displayed the live processed webcam feed.

# Mini Project

## Real-Time Video Processing Tool
The application performs the following tasks:
* Reads a recorded video.
* Displays the original video.
* Converts each frame to grayscale.
* Applies Gaussian Blur.
* Applies Canny Edge Detection.
* Displays the processed video in real time.
* Saves the processed video automatically.
* Supports real-time webcam processing using the same techniques.

# Challenge Task
Processed **3 different videos**.
For each video, the following outputs were generated:

* Original Video
* Processed Video
* Comparison of original and processed result

# How OpenCV Reads Videos
OpenCV reads a video using the `VideoCapture()` function. A video is made up of multiple image frames. OpenCV reads one frame at a time inside a loop, allowing each frame to be processed individually before displaying or saving it.

# What FPS Means
FPS (Frames Per Second) represents the number of frames displayed in one second of a video. It determines how smooth the video appears. While saving processed videos, using the original FPS helps maintain the same playback speed.

# Processing Techniques Applied

The following processing techniques were applied to every video frame:
* Grayscale Conversion
* Gaussian Blur
* Canny Edge Detection
* Real-Time Video Display
* Processed Video Saving

# Challenges Faced

* Understanding that videos are processed frame by frame instead of as a whole.
* Learning how to use `VideoCapture()` and `VideoWriter()`.
* Resolving file path issues while reading videos.
* Handling codec compatibility issues while saving processed videos.
* Displaying high-resolution videos properly without affecting the saved output.
* Maintaining the original FPS and video quality while processing frames.

# Learning Outcome
After completing this task, I can:
* Read videos using OpenCV.
* Process videos frame by frame.
* Retrieve video properties such as FPS, width, height, and total frames.
* Apply grayscale conversion, Gaussian Blur, and Canny Edge Detection to videos.
* Capture and process live webcam video.
* Save processed videos automatically.
* Build a complete real-time video processing application using OpenCV.
* Process multiple videos and compare the original and processed outputs.
