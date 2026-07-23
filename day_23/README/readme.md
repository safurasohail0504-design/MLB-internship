# Day 23 – Computer Vision Image Processing Studio

## Overview

In this task, I combined multiple Computer Vision techniques into a single interactive application using **OpenCV** and **Gradio**. The application allows users to upload an image, select an image processing operation, instantly view the processed result, and download the output image through a simple web interface.


## Technologies Used

- Python
- OpenCV
- NumPy
- Gradio

## Project Structure

Day_23
│
├── Source Code
│   ├── grayscale.py
│   ├── blur.py
│   ├── edge_detection.py
│   ├── rotation.py
│   ├── brightness.py
│   ├── contour_detection.py
│   ├── image_flip.py
│   └── thresholding.py
│
├── app.py
├── requirements.txt
├── README.md
├── Sample Input Images
├── Sample Output Images

## Coding Practice Completed

The Gradio application allows the user to:
- Upload an image
- Select an image processing operation
- Process the image
- View the processed result
- Download the processed image

## Image Processing Operations

The application includes the following operations:

- Grayscale Conversion
- Gaussian Blur
- Edge Detection (Canny)
- Image Rotation
- Brightness Adjustment
- Contour Detection
- Image Flip
- Thresholding

## Mini Project

### Computer Vision Image Processing Studio

The application performs the following tasks:
- Uploads an image
- Applies different OpenCV image processing techniques
- Displays the original and processed images
- Allows users to download the processed image
- Provides a simple and user-friendly Gradio interface

## Challenge Task

Implemented additional image processing features that were not covered during the coding practice.

### Custom Features
- Image Flip
- Thresholding

These features make the application more useful and interactive.

## How Gradio Works

Gradio is a Python library that creates a web interface directly from Python code.
Instead of building HTML, CSS, and JavaScript manually, Gradio automatically generates an interactive web application.
Users simply upload an image, choose an operation, and Gradio sends the image to the Python function, processes it using OpenCV, and displays the output.

## Image Processing Techniques Used

- Grayscale Conversion
- Gaussian Blur
- Canny Edge Detection
- Image Rotation
- Brightness Adjustment
- Contour Detection
- Image Flip
- Binary Thresholding

## Challenges Faced

- Understanding how Gradio components communicate with Python functions.
- Learning to organize multiple image processing operations inside a single application.
- Handling grayscale and color image outputs correctly.
- Deploying the application on Hugging Face because the account only allowed Static Spaces while Gradio Spaces required additional permissions.

## Learning Outcome

After completing this task, I can:

- Build an interactive Computer Vision application.
- Create user interfaces using Gradio.
- Apply multiple OpenCV image processing techniques.
- Process uploaded images in real time.
- Organize Computer Vision projects professionally.
- Prepare AI applications for deployment on Hugging Face Spaces.

## Future Improvements

- Add more image processing filters.
- Support webcam image capture.
- Allow applying multiple filters together.
- Improve the interface with additional customization options.
- Deploy the application publicly on Hugging Face Spaces.