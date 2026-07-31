# Day 29 – Custom Helmet Detection using YOLO

## Project Introduction

This project demonstrates a **Custom Helmet Detection System** using **YOLOv8** and **Streamlit**. A custom YOLO model was trained on the Helmet Detection dataset downloaded from **Roboflow Universe**. The application allows users to upload an image, detect helmets, display bounding boxes with confidence scores, preview the prediction, and download the processed image.

The project was developed as part of the **MLB AI Internship Day 29** task and focuses on understanding the complete workflow of custom object detection, including dataset preparation, model training, evaluation, inference, and deployment.

---

# Technologies Used

* Python
* Ultralytics YOLOv8
* OpenCV
* NumPy
* Pillow
* Streamlit
* Roboflow Universe

---

# Folder Structure

```text
Day_29

├── YOLO Training Script
│   ├── dataset_structure.py
│   ├── explore_yaml.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── inference.py
│
├── Sample Test Images
├── Prediction Results
├── best.pt
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
* Detect helmets using the trained YOLO model
* Draw bounding boxes
* Display detected class names
* Display confidence scores
* Preview the prediction
* Download the processed image

---

# What is Object Detection?

Object Detection is a Computer Vision task that identifies one or more objects present in an image and determines their exact locations by drawing bounding boxes.

Unlike image classification, object detection answers:

* What object is present?
* Where is the object located?

Applications include:

* Workplace Safety
* Construction Site Monitoring
* Traffic Monitoring
* Security Surveillance
* Robotics
* Autonomous Vehicles

---

# How YOLO is Different from Image Classification

### Image Classification

* Predicts only one label for the entire image.
* Does not locate objects.
* Produces a single output class.

Example:

```
Image → Helmet
```

---

### YOLO

* Detects multiple objects.
* Predicts class names.
* Draws bounding boxes.
* Displays confidence scores.
* Performs detection in one forward pass, making it fast.

Example:

```
Helmet (97%)
Helmet (93%)
```

---

# Dataset Selected

For this project, the **Helmet Detection Dataset** from **Roboflow Universe** was selected.

Reason for choosing this dataset:

* Practical real-world safety application.
* Suitable for learning custom object detection.
* Contains helmet and non-helmet examples.
* Well organized in YOLO format.

---

# YOLO Model Used

The project uses **YOLOv8 Nano (yolov8n.pt)** as the base model for transfer learning.

Reasons:

* Lightweight
* Fast training
* CPU friendly
* Beginner friendly
* Good balance between speed and accuracy

---

# Coding Practice

Separate scripts were created to understand every stage of custom YOLO training.

### dataset_structure.py

* Explore dataset folders.
* Verify image and label structure.

### explore_yaml.py

* Read and understand the data.yaml file.

### train_model.py

* Train the custom YOLO model.

### evaluate_model.py

* Evaluate the trained model.
* Display Precision, Recall and mAP.

### inference.py

* Run inference on sample test images.
* Save prediction results.

---

# Mini Project

## Custom Helmet Detection System

The Streamlit application performs the following tasks:

* Upload an image
* Detect helmets
* Display original image
* Display prediction result
* Show class names
* Show confidence scores
* Download processed image

---

# Training Configuration

* Dataset: Helmet Detection Dataset
* Base Model: YOLOv8 Nano
* Epochs: 20
* Batch Size: 8
* Image Size: 640 × 640

---

# Final Evaluation Metrics

*(Update after training completes.)*

* mAP@50:
* mAP@50-95:
* Precision:
* Recall:

---

# Sample Test Images

The trained model was tested on **10 images**, including:

* 5 images containing helmets.
* 5 images without helmets.

---

# Prediction Results

The trained model successfully generated prediction images by:

* Detecting helmets.
* Drawing bounding boxes.
* Displaying confidence scores.
* Saving processed prediction images.

---

# How to Run the Project

### Clone Repository

```bash
git clone <repository_link>
```

### Open Project Folder

```bash
cd Day_29
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Coding Practice Scripts

```bash
python "YOLO Training Script/dataset_structure.py"

python "YOLO Training Script/explore_yaml.py"

python "YOLO Training Script/train_model.py"

python "YOLO Training Script/evaluate_model.py"

python "YOLO Training Script/inference.py"
```

### Run Streamlit Application

```bash
streamlit run app.py
```

---

# Challenges Faced

During this task, I faced several challenges:

* Understanding the YOLO dataset structure.
* Learning the purpose of the data.yaml file.
* Training the model on CPU, which required more time.
* Understanding evaluation metrics like mAP, Precision and Recall.
* Building an inference application using the trained custom model.
* Managing prediction outputs and organizing project files.

---

# What I Learned

After completing this task, I learned how to:

* Prepare datasets for YOLO training.
* Understand YOLO annotation format.
* Configure the data.yaml file.
* Train a custom object detection model.
* Evaluate model performance.
* Run inference using a trained model.
* Build a Streamlit application using a custom YOLO model.
* Organize a complete Computer Vision project professionally.

---

# Possible Improvements

In future versions, I would like to add:

* Live webcam helmet detection.
* Video inference support.
* Adjustable confidence threshold.
* Multiple image upload.
* Real-time detection dashboard.
* Better UI design.
* GPU training for faster convergence.
* Hyperparameter tuning to improve model accuracy.