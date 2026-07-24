# Day 24 – OCR Document Reader using EasyOCR

## Project Introduction

This project demonstrates the basics of **Optical Character Recognition (OCR)** using **EasyOCR**. The application extracts text from images such as documents, invoices, receipts, signboards, book pages, and handwritten notes. It also applies simple image preprocessing techniques to improve OCR accuracy and provides a Streamlit interface for easy interaction.

# Tools and Libraries

* Python 3.11
* EasyOCR
* OpenCV
* NumPy
* Matplotlib
* Streamlit

# Folder Structure
Day_24
│
├── OCR Practice Scripts
│   ├── read_single_image.py
│   ├── grayscale_ocr.py
│   ├── threshold_ocr.py
│   ├── image_enhancement.py
│   └── compare_results.py
│
├── Mini Project Source Code
│   └── ocr_reader.py
│
├── Sample Input Images
│
├── Extracted Text Files
|__ runtime.txt
├── app.py
├── requirements.txt
├── README.md
├── GitHub Repository Link.txt
└── Streamlit App Link.txt

# Practice Tasks Completed
The following OCR practice scripts were created:

### 1. Read Single Image
* Read text from one image
* Display extracted text

### 2. Grayscale OCR
* Convert image into grayscale
* Extract text after preprocessing

### 3. Threshold OCR
* Apply binary thresholding
* Compare OCR accuracy

### 4. Image Enhancement
* Improve image quality
* Apply OCR on enhanced image

### 5. Compare Results
* Compare OCR output from:

  * Original Image
  * Grayscale Image
  * Threshold Image
  * Enhanced Image

# Mini Project

## Simple OCR Document Reader

The application performs the following tasks:

* Upload an image
* Display the original image
* Extract all visible text using EasyOCR
* Display extracted text
* Save extracted text into a `.txt` file
* Download the generated text file

# Features

* Upload JPG/JPEG/PNG images
* OCR using EasyOCR
* Preview original image
* Display extracted text
* Save output as TXT
* Download extracted text
* Simple Streamlit interface

# Image Preprocessing Used

To improve OCR accuracy, the following preprocessing techniques were tested:

* Grayscale Conversion
* Binary Thresholding
* Image Enhancement

These preprocessing methods helped EasyOCR detect text more accurately, especially on documents with uneven lighting.

# Dataset Used

The project was tested on more than **15 text-based images**, including:

* Printed Documents
* Receipts
* Invoices
* Signboards
* Book Pages
* Medicine Labels
* Forms
* Certificates
* Handwritten Notes
* ID-style Documents

The images also included different:

* Text sizes
* Fonts
* Lighting conditions
* Background colors

# How to Run the Project

## 1. Clone the Repository

```bash
git clone <repository_link>
```
## 2. Open Project Folder

```bash
cd Day_24
```
## 3. Install Required Libraries

```bash
pip install -r requirements.txt
```
## 4. Run Practice Scripts
Example:

```bash
python "OCR Practice Scripts/read_single_image.py"
```
## 5. Run Mini Project

```bash
python "Mini Project Source Code/ocr_reader.py"
```
## 6. Run Streamlit Application

```bash
streamlit run app.py
```
The application will open automatically in your browser.
# Streamlit Application

The deployed application allows users to:

* Upload an image
* View the original image
* Extract text instantly
* Save extracted text
* Download the text file

# Challenges Faced

* Installing EasyOCR and its dependencies.
* Improving OCR accuracy on images with low contrast.
* Comparing preprocessing techniques to achieve better results.
* Deploying the Streamlit application successfully.

# What I Learned

After completing this task, I learned how to:
* Understand the working of OCR.
* Extract text using EasyOCR.
* Improve OCR accuracy using preprocessing.
* Compare OCR outputs on different images.
* Build a complete OCR application.
* Deploy an OCR project using Streamlit.

# Future Improvements

In future versions, I would like to add:
* Multiple language support
* PDF document OCR
* Camera image capture
* Batch image processing
* Text translation
* Export extracted text to PDF and Word
