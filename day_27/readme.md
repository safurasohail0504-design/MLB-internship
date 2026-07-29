
# Day 27 – Document & Object Segmentation Tool

## Project Introduction

This project demonstrates a simple **Image Segmentation Tool** using OpenCV and Streamlit. The application allows users to upload an image, apply different thresholding techniques, separate the foreground object from the background, preview the segmented output, and download the processed image.

The project was developed as part of the **MLB AI Internship Day 27** task and focuses on basic image segmentation techniques that are commonly used as preprocessing steps in Computer Vision.

---

# Technologies Used

* Python
* OpenCV
* NumPy
* Streamlit

---

# Folder Structure

```
Day_27

├── Segmentation Scripts
│   ├── grayscale.py
│   ├── binary.py
│   ├── adaptive.py
│   ├── otsu.py
│   ├── foreground.py
│   └── compare.py
│
├── Sample Input Images
├── Output Images
├── app.py
├── requirements.txt
├── README.md
├── GitHub Repository Link.txt
└── Streamlit App URL.txt
```

---

# Features

The application can:

* Upload an image
* Apply Binary Thresholding
* Apply Adaptive Thresholding
* Apply Otsu Thresholding
* Perform simple Foreground Segmentation
* Display the segmented image
* Download the processed image

---

# What is Image Segmentation?

Image Segmentation is a Computer Vision technique used to divide an image into different regions or groups of pixels. The main goal is to separate the foreground object from the background so that important parts of the image can be analyzed more easily.

It is commonly used in:

* Medical image analysis
* Self-driving cars
* Agriculture
* Image editing
* Object recognition

---

# Difference Between Binary, Adaptive, and Otsu Thresholding

### Binary Thresholding

* Uses one fixed threshold value.
* Pixels above the threshold become white.
* Pixels below the threshold become black.
* Works well when lighting is uniform.

---

### Adaptive Thresholding

* Calculates threshold values for different image regions.
* Handles uneven lighting conditions.
* Produces better results for documents with shadows.

---

### Otsu Thresholding

* Automatically calculates the best threshold value.
* No manual threshold selection is required.
* Performs well when the object and background have clear intensity differences.

---

# Coding Practice

Separate scripts were created to understand each segmentation technique individually.

### grayscale.py

* Reads an image
* Converts it to grayscale
* Saves the grayscale image

### binary.py

* Applies Binary Thresholding
* Saves the output image

### adaptive.py

* Applies Adaptive Thresholding
* Saves the output image

### otsu.py

* Applies Otsu Thresholding
* Saves the output image

### foreground.py

* Performs simple foreground segmentation
* Saves the segmented image

### compare.py

* Displays the outputs of Binary, Adaptive, and Otsu Thresholding side by side for comparison

---

# Mini Project

## Document & Object Segmentation Tool

The Streamlit application performs the following tasks:

* Upload an image
* Select a segmentation method
* Display the original image
* Display the segmented output
* Download the processed image

---

# Dataset Used

The application was tested on **15 images**, including:

* Documents
* Books
* Laptop
* Mobile Phone
* Keyboard
* Mouse
* Mug
* Water Bottle
* Product Box
* Building
* Images with uneven lighting
* Images containing shadows

---

# Which Method Worked Best and Why?

For my dataset, **Adaptive Thresholding** produced the best overall results.

It handled uneven lighting, shadows, and different document backgrounds much better than Binary Thresholding. Binary Thresholding worked well only when lighting was uniform, while Otsu Thresholding performed well on high-contrast images but struggled with shadows.

Because my dataset contained images captured under different lighting conditions, Adaptive Thresholding gave the most consistent segmentation results.

---

# How to Run the Project

### Clone Repository

```bash
git clone <repository_link>
```

### Open Project Folder

```bash
cd Day_27
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Coding Practice Scripts

```bash
python "Segmentation Scripts/grayscale.py"

python "Segmentation Scripts/binary.py"

python "Segmentation Scripts/adaptive.py"

python "Segmentation Scripts/otsu.py"

python "Segmentation Scripts/foreground.py"

python "Segmentation Scripts/compare.py"
```

### Run Streamlit Application

```bash
streamlit run app.py
```

---

# Challenges Faced

During this task, I faced several challenges:

* Understanding the differences between Binary, Adaptive, and Otsu Thresholding.
* Choosing the most suitable segmentation method for different images.
* Handling images with shadows and uneven lighting.
* Initially facing Streamlit launch issues due to running the application from the wrong working directory.
* Configuring and deploying the Streamlit application successfully.

---

# What I Learned

After completing this task, I learned how to:

* Understand the basics of Image Segmentation.
* Apply different thresholding techniques using OpenCV.
* Compare Binary, Adaptive, and Otsu Thresholding.
* Separate foreground objects from the background.
* Build an interactive Streamlit application.
* Organize and deploy a Computer Vision project professionally.

---

# Possible Improvements

In future versions, I would like to add:

* Watershed Segmentation
* GrabCut Background Removal
* Deep Learning-based Segmentation (Mask R-CNN)
* Multiple image processing support
* Live camera segmentation
* Automatic best-threshold selection
* Better visualization of segmented objects