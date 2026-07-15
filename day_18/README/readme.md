#  Day 18 - OpenCV Fundamentals & Basic Image Processing

## Project Overview
This project was completed as part of the MLB AI Internship Day 18 task.
The goal of this project was to learn the fundamentals of OpenCV and understand how images can be processed using Python.
The project includes practice programs for common image processing operations and a menu-driven Image Processing Toolkit.

# 📂 Project Structure
Day_18/
│
├── OpenCV Practice Problems/
│   ├── read_display.py
│   ├── color_to_gray.py
│   ├── resize.py
│   ├── crop.py
│   ├── rotate.py
│   ├── flip.py
│   ├── draw_shapes.py
│   └── add_text.py
│
├── Image Processing Toolkit/
│   └── mini_project.py
│
├── sample images/
│   ├── img1.jpg
│   └── img2.jpg
│
├── output/
│   ├── grayscale.jpg
│   ├── resized.jpg
│   ├── rotated.jpg
│   ├── flipped.jpg
│   ├── cropped.jpg
│   ├── shapes.jpg
│   ├── text.jpg
│   └── project-output.jpg
│
└── README.md

# Topics Covered:
- Reading Images
- Displaying Images
- Saving Images
- Image Properties
- BGR vs RGB
- Grayscale Images
- Image Resizing
- Cropping
- Rotating
- Flipping
- Drawing Shapes
- Adding Text
- Menu Driven OpenCV Application

# Requirements
- Python 3.11+
- OpenCV
- NumPy

Install the required libraries using:
pip install opencv-python
pip install numpy
or
pip install opencv-python numpy

#  How to Run:
1. Clone the repository
2. Open the Day_18 folder.
3. Install the required libraries.
4. Run any practice file.
Example:
python read_display.py
To run the mini project:
python mini_project.py

# Coding Practice:
The following OpenCV programs were implemented:
- Read image and display image information
- Convert image to grayscale
- Resize image
- Crop image
- Rotate image
- Flip image
- Draw rectangle, circle, line, and polygon
- Add custom text
- Save processed images

#  Mini Project:
## Image Processing Toolkit
A menu-driven application that allows the user to perform different image processing operations.

### Features:
- Load Image
- Convert to Grayscale
- Resize Image
- Rotate Image
- Flip Image
- Crop Image
- Draw Shapes
- Add Text
- Save Processed Image

# Difference Between BGR and RGB:
Both BGR and RGB are color formats used to represent images.
RGB (Red, Green, Blue):
- Stores colors in the order:
  - Red
  - Green
  - Blue
- Used by most image processing libraries and image viewers such as Matplotlib.
Example:
(255, 0, 0) means Red.
BGR (Blue, Green, Red)
- Stores colors in the order:
  - Blue
  - Green
  - Red
- This is the default color format used by OpenCV.
Example:
(255, 0, 0)means Blue in OpenCV.

# What are Grayscale Images?
A grayscale image contains only shades of gray instead of colors.
Each pixel stores only one intensity value ranging from:
- 0 → Black
- 255 → White
instead of three color channels.

Why Grayscale Images are Used:
- Faster image processing
- Less memory usage
- Reduces computational cost
- Commonly used before edge detection and object detection
- Simplifies Computer Vision tasks

#  OpenCV Functions Used
| Function | Purpose |
|----------|---------|
| cv2.imread() | Read an image |
| cv2.imshow() | Display image |
| cv2.imwrite() | Save image |
| cv2.waitKey() | Wait for keyboard input |
| cv2.destroyAllWindows() | Close image windows |
| cv2.cvtColor() | Convert color spaces |
| cv2.resize() | Resize image |
| cv2.rotate() | Rotate image |
| cv2.flip() | Flip image |
| cv2.rectangle() | Draw rectangle |
| cv2.circle() | Draw circle |
| cv2.line() | Draw line |
| cv2.polylines() | Draw polygon |
| cv2.putText() | Add text to image |

# Challenges Faced:
During the project, I faced several issues while working with OpenCV.
### 1. Image Not Loading
OpenCV showed:
can't open/read file
Solution:
Used the correct image path and verified the image extension (.jpg/.jpeg).

### 2. Unicode Path Error
Problem:
Windows paths using backslashes generated:
unicodeescape codec error
Solution:
Used either:
python
r"C:\folder\image.jpg"
or
python
"C:/folder/image.jpg"

# Learning Outcomes
By completing this project, I learned:
- Image representation in OpenCV
- Difference between BGR and RGB
- Grayscale image conversion
- Basic image transformations
- Drawing shapes on images
- Adding text to images
- Saving processed images
- Building a menu-driven image processing application using Python and OpenCV