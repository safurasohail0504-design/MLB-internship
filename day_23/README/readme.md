# Day 23 – Computer Vision Image Processing Studio

## Project Introduction

This project combines different image processing techniques into one simple application. It is built using **Python**, **OpenCV**, **NumPy**, and **Streamlit**. The application allows users to upload an image, choose a processing operation, preview the result, and download the processed image with a custom file name.

## Tools and Libraries

- Python
- OpenCV
- NumPy
- Streamlit

## Folder Structure

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
├── README
├── Sample Input Images
└── Sample Output Images

## Features of the Application

The application provides the following functionality:
- Upload an image
- Select an image processing operation
- View the processed image instantly
- Enter a custom output file name
- Save the processed image
- Download the processed image

## Image Processing Operations

The following operations are available inside the application:
- Grayscale Conversion
- Gaussian Blur
- Edge Detection
- Image Rotation
- Brightness Adjustment
- Contour Detection
- Image Flip
- Thresholding

## Mini Project

### Computer Vision Image Processing Studio

This application combines all the OpenCV techniques learned during previous tasks into one user-friendly interface.
It performs the following tasks:
- Reads an uploaded image
- Processes the image according to the selected operation
- Displays both original and processed images
- Saves the processed result
- Allows downloading the final image

## Challenge Task

Two additional features were added to improve the application:
- Image Flip
- Thresholding
These features were implemented as custom additions beyond the basic requirements.

## How the Application Works

1. The user uploads an image.
2. An image processing operation is selected from the dropdown menu.
3. The application processes the image using OpenCV.
4. The processed image is displayed on the screen.
5. The user enters a file name.
6. The image is saved and can also be downloaded.

## Techniques Used

The project includes the following Computer Vision techniques:
- Color to Grayscale Conversion
- Gaussian Blurring
- Canny Edge Detection
- Image Rotation
- Brightness Enhancement
- Contour Detection
- Horizontal Image Flipping
- Binary Thresholding

## Difficulties Faced

During this task, I faced a few challenges:

- Converting the Gradio application into a Streamlit application.
- Implementing image saving with a custom file name instead of using a fixed name.
- Deploying the application because new Hugging Face accounts only supported Static Spaces instead of Gradio Spaces.

## What I Learned

After completing this task, I learned how to:
- Build a complete Computer Vision application.
- Create a graphical interface using Streamlit.
- Integrate multiple OpenCV operations into one project.
- Save and download processed images.
- Organize project files professionally for deployment.

## Future Improvements
In future versions, I would like to add:
- Contrast Adjustment
- Image Sharpening
- Multiple filters applied together
- Crop and Resize options
- Webcam image processing support