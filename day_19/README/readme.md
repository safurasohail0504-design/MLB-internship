# Day-19: Image Transformation and Document Image Enhancement using OpenCV

## Overview

This project demonstrates various image transformation and image enhancement techniques using OpenCV in Python. It also includes a Document Image Enhancement Tool that automatically improves the quality of scanned and tilted document images.

## Image Transformations Implemented

### 1. Translation
Moves an image horizontally and vertically without changing its size.

### 2. Rotation
Rotates an image at different angles (30°, 45°, and 60°).

### 3. Scaling
Resizes an image by increasing and decreasing its dimensions.

### 4. Affine Transformation
Applies geometric transformation while preserving parallel lines.

### 5. Perspective Transformation
Corrects the perspective of tilted document images to obtain a top-down view.

## Image Enhancement Techniques

### 1. Grayscale Conversion
Converts the image into grayscale for easier processing.

### 2. Gaussian Blur
Reduces image noise and smooths the image.

### 3. Median Blur
Removes salt-and-pepper noise while preserving edges.

### 4. Bilateral Filter
Reduces noise while keeping edges sharp.

### 5. Brightness Adjustment
Increases or decreases image brightness for better visibility.

### 6. Contrast Adjustment
Improves the difference between light and dark regions, making text more readable.

### 7. Image Sharpening
Enhances edges and fine details using a sharpening kernel.

## Document Image Enhancement Tool

The application performs the following steps:

1. Load the document image.
2. Detect the document automatically.
3. Correct the document perspective.
4. Convert the image to grayscale.
5. Reduce image noise using Gaussian Blur.
6. Increase brightness.
7. Improve contrast.
8. Sharpen the document.
9. Save the final enhanced image.

The tool supports multiple document images and processes them individually.

## Transformation with the Biggest Impact

Perspective Transformation had the biggest impact on document quality because it corrected tilted documents into a properly aligned top-down view, making the text easier to read and improving the effectiveness of all subsequent enhancement techniques.

## Challenges Faced

- Detecting the correct document boundary for different document types.
- Handling images with different sizes, formats, and lighting conditions.
- Preventing incorrect perspective correction on small objects inside documents.
- Ensuring the complete document remained visible after perspective correction.
- Selecting suitable brightness and contrast values that worked well for different images.

## Tools Used

- Python
- OpenCV
- NumPy

## Project Structure

```
Day-19
│
├── Image Transformation Scripts
├── Image Enhancement Scripts
├── Document Image Enhancement Tool
├── Input Images
├── Enhanced Output Images
├── README.md


## Learning Outcomes

- Applied common image transformation techniques using OpenCV.
- Enhanced image quality using multiple preprocessing methods.
- Understood the importance of image preprocessing in Computer Vision.
- Built a reusable document image enhancement pipeline for scanned and tilted documents.