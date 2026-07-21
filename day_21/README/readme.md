# Day 21 – Contours and Shape Detection

## Overview
In this task, I learned how to detect contours and identify different geometric shapes using OpenCV. I implemented contour detection, calculated the area and perimeter of objects, drew bounding rectangles, detected common shapes, and built a Shape Detection System that labels shapes and displays their measurements.

## Technologies Used
* Python
* OpenCV
* NumPy

## Project Structure
Day_21
│
├── Contour Detection Script
├── Shape Detection Script
├── Challenge Task
├── Input Images
├── Output Images
├── README.md

## Coding Practice completed

### Contour Detection
* Loaded an image using OpenCV.
* Converted the image to grayscale.
* Applied thresholding to separate objects from the background.
* Detected contours using `findContours()`.
* Drew all detected contours on the image.

### Area and Perimeter Calculation
* Calculated the area of each contour using `cv2.contourArea()`.
* Calculated the perimeter using `cv2.arcLength()`.
* Filtered small contours to reduce noise.

### Bounding Rectangle
* Drew a bounding rectangle around each detected object.
* Used the rectangle coordinates for further shape detection.

### Shape Detection
* Detected different geometric shapes based on the number of contour vertices.
* Classified objects as Triangle, Square, Rectangle, Pentagon, Hexagon, Circle, or Polygon.
* Displayed the detected shape name along with its area and perimeter.

## Mini Project

### Shape Detection System
The application performs the following tasks:
* Loads an image.
* Detects all contours.
* Identifies geometric shapes.
* Draws contours around each shape.
* Labels every detected shape.
* Displays the area and perimeter of each shape.
* Saves the final output image automatically.

## Challenge Task
Tested the application on 10 different images.
For every image, the following outputs were generated:
* Original Image
* Contour Detection Result
* Final Shape Detection Result with Labels

## What are Contours?
Contours are the boundaries or outlines of objects in an image. They are used to identify the shape, size, and position of objects and are an important concept in computer vision.

## How Contour Detection Works
* Convert the image to grayscale.
* Apply thresholding to separate the object from the background.
* Use `findContours()` to detect object boundaries.
* Draw the detected contours and analyze them for shape detection.

## Shapes Detected
The program can detect:
* Triangle
* Square
* Rectangle
* Circle
* Pentagon
* Hexagon
* Polygon

## Challenges Faced
* Finding images with clean backgrounds for accurate shape detection.
* Removing small noisy contours that affected detection accuracy.
* Adjusting threshold values to correctly separate objects from the background.
* Correctly distinguishing between squares and rectangles using the aspect ratio.

## Learning Outcome
After completing this task, I can:
* Detect contours in images using OpenCV.
* Calculate the area and perimeter of detected objects.
* Draw bounding rectangles around objects.
* Identify common geometric shapes.
* Build a complete Shape Detection System using OpenCV.
* Process multiple images and save contour and shape detection results automatically.