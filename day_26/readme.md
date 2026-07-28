# Day 26 – Image Feature Matching System

## Project Introduction

This project demonstrates an Image Feature Matching System using OpenCV, ORB (Oriented FAST and Rotated BRIEF), and Streamlit. The application allows users to upload two similar images, detect important image features, match those features, visualize the matched keypoints, and download the final matched image.
The project was developed as part of the MLB AI Internship Day 26 task and focuses on Feature Detection and Feature Matching techniques used in Computer Vision.

# Technologies Used

- Python
- OpenCV
- NumPy
- Streamlit

# Folder Structure

Day_26

├── Feature Detection Scripts
│   ├── harris.py
│   ├── orb.py
│   └── compare.py
│
├── Feature Matching Scripts
│   ├── brute_force.py
│   └── knn.py
│
├── Sample Image Pairs
├── Output Images
├── app.py
├── requirements.txt
├── README.md
├── GitHub Repository Link.txt
└── Streamlit App URL.txt


# Features

The application can:
- Upload two similar images
- Detect ORB keypoints
- Match image features using Brute Force Matcher
- Display original images
- Display matched features
- Show total keypoints detected in both images
- Show total feature matches
- Download the matched image

# What are Image Features?

Image features are unique points in an image such as corners, edges, textures, or patterns that help identify an object. These features remain recognizable even if the object is viewed from different angles or distances, making them useful for image matching and object recognition.

# Difference Between Harris Corner Detection and ORB

### Harris Corner Detection

- Detects only corner points.
- Does not generate descriptors.
- Cannot perform feature matching directly.
- Mainly used for corner detection.

### ORB (Oriented FAST and Rotated BRIEF)

- Detects keypoints.
- Generates feature descriptors.
- Supports feature matching between images.
- Faster and more suitable for real-time Computer Vision applications.

# How Feature Matching Works

Feature matching follows these steps:

1. Upload two similar images.
2. Convert both images to grayscale.
3. Detect keypoints using ORB.
4. Generate descriptors for both images.
5. Match descriptors using Brute Force Matcher.
6. Sort and display the best matches.
7. Show the matched image along with keypoint statistics.

# Coding Practice

Separate scripts were created to understand each concept individually.

### harris.py

- Reads an image.
- Detects Harris Corners.
- Highlights detected corners.
- Saves the output image.

### orb.py

- Detects ORB keypoints.
- Draws detected keypoints.
- Saves the output image.

### compare.py

- Displays Harris and ORB outputs side by side for comparison.

### brute_force.py

- Matches ORB descriptors using Brute Force Matcher.
- Displays total keypoints and matches.
- Saves the matched image.

### knn.py

- Performs feature matching using KNN Matcher.
- Filters good matches using Lowe's Ratio Test.
- Saves the output image.

# Mini Project

## Image Feature Matching System

The Streamlit application performs the following tasks:

- Upload Image 1
- Upload Image 2
- Detect ORB keypoints
- Match image features
- Display original images
- Display matched image
- Show total keypoints detected
- Show total good matches
- Download the matched image

# Dataset Used

The application was tested on 10 image pairs including:

- Books
- Laptop
- Keyboard
- Mouse
- Mug
- Mobile Phone
- Water Bottle
- Building
- Product Box

# Which Image Pair Produced the Best Matching Results and Why?

The **Laptop image pair** produced the best matching results because both images contained many unique edges, corners, and textured regions. ORB was able to detect a large number of stable keypoints, resulting in more accurate feature matching compared to smoother objects.

# How to Run the Project

### Clone Repository

```bash
git clone <repository_link>
```

### Open Project Folder

```bash
cd Day_26
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Coding Practice Scripts

```bash
python "Feature Detection Scripts/harris.py"

python "Feature Detection Scripts/orb.py"

python "Feature Detection Scripts/compare.py"

python "Feature Matching Scripts/brute_force.py"

python "Feature Matching Scripts/knn.py"
```

### Run Streamlit Application

```bash
streamlit run app.py
```
# Challenges Faced

During this task, I faced several challenges:

- Understanding the difference between Harris Corner Detection and ORB.
- Learning how descriptors are matched using Brute Force Matcher.
- Selecting suitable image pairs for better matching results.
- Displaying matched features correctly in Streamlit.
- Deploying the application successfully.

# What I Learned

After completing this task, I learned how to:

- Detect important image features.
- Compare Harris Corner Detection and ORB.
- Match image features using Brute Force Matcher.
- Build an interactive Streamlit application.
- Visualize feature matching results.
- Organize a Computer Vision project professionally.

# Possible Improvements

In future versions, I would like to add:

- SIFT Feature Detection
- SURF Feature Detection
- FLANN Matcher
- Real-time camera feature matching
- Support for multiple matching algorithms
- Improved matching visualization
- Better filtering of incorrect matches