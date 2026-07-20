# Day 20 – Edge Detection and Morphological Operations

## Overview
In this task, I learned how to detect document boundaries using OpenCV by applying different edge detection and morphological operations. I implemented various image processing techniques and built a Document Boundary Detection Tool that detects and highlights document boundaries from multiple document images.

## Technologies Used
* Python
* OpenCV
* NumPy

## Project Structure
day_20
│
├── edge detection scripts
├── morphological operations scripts
├── document boundary detection tool
├── challenge task
├── input images
├── output images
├── README.md

## Edge Detection Techniques

### Sobel Operator
* Detects horizontal and vertical edges separately.
* Useful for finding edge direction.
* Produces smoother edge detection than simple gradients.

### Laplacian Operator
* Detects edges in all directions using second-order derivatives.
* Highlights fine details and sharp intensity changes.
* More sensitive to image noise.

### Canny Edge Detection
* Uses Gaussian Blur, gradient calculation, non-maximum suppression, and thresholding.
* Produces thin, accurate, and continuous edges.
* Provided the best results for document boundary detection.

## Morphological Operations

### Erosion
* Removes small white noise.
* Shrinks object boundaries.

### Dilation
* Expands object boundaries.
* Connects broken edge segments.

### Opening
* Removes small noise while preserving the main object.
* Useful for cleaning images.

### Closing
* Fills small gaps and holes inside object boundaries.
* Helped create continuous document edges.

### Morphological Gradient
* Displays only the outline of objects.
* Useful for emphasizing boundaries.

### Top Hat
* Extracts small bright objects from the background.
* Useful for highlighting light details.

### Black Hat
* Extracts dark objects from a bright background.
* Useful for detecting dark regions.

## Mini Project

### Document Boundary Detection Tool
The application performs the following steps:
* Loads document images.
* Converts images to grayscale.
* Applies Gaussian Blur.
* Detects edges using Canny Edge Detection.
* Applies morphological closing, dilation, and erosion.
* Detects the document contour.
* Draws the detected boundary on the original image.
* Saves the processed output images.

## Challenge Task
Processed 10 different document images.
For each document, the following outputs were generated:
* Original Image
* Edge Detection Result
* Morphological Operation Result
* Final Image with Detected Document Boundary

## Best Combination of Techniques
The combination of Gaussian Blur, Canny Edge Detection, Morphological Closing, Dilation, and Erosion produced the best document boundary detection results because it reduced noise, connected broken edges, and generated clear document contours.

## Challenges Faced
* Some document images contained laptops, keyboards, pens, or other objects that interfered with contour detection.
* Images with poor lighting or weak document boundaries were difficult to detect accurately.
* Selecting suitable Canny threshold values and contour area limits required multiple experiments.
* Different image formats and backgrounds affected the boundary detection performance.

## Learning Outcome
After completing this task, I can:
* Perform edge detection using Sobel, Laplacian, and Canny.
* Apply different morphological operations for image preprocessing.
* Detect document boundaries using contours.
* Build a complete document boundary detection pipeline using OpenCV.
* Understand how preprocessing improves document analysis and computer vision tasks.