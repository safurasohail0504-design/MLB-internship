# Day 25 – Document OCR Web Application

## Project Introduction

This project demonstrates a complete Optical Character Recognition (OCR) pipeline using **EasyOCR** and **Gradio**. The application allows users to upload a document image, preprocess it for better text recognition, extract readable text, preview the results, and download the extracted text as a `.txt` file.

The project was built as part of the MLB AI Internship Day 25 task and combines image preprocessing with OCR inside an interactive web application.

# OCR Library Used
This project uses:
- **EasyOCR**
EasyOCR was selected because it is simple to use, supports multiple languages, and performs well on different document types without requiring model training.

# Technologies Used

- Python
- EasyOCR
- OpenCV
- NumPy
- Gradio
# Folder Structure
Day_25

├── OCR Source Code
│   ├── processing.py
│   ├── ocr_engine.py
│   ├── save_text.py
│
├── Sample Input Images
│
├── Sample Output Results
│
├── app.py
├── requirements.txt
├── README.md
├── GitHub Repository Link.txt
└── ngrok Public URL.txt
# Features

The application can:
- Upload document images
- Apply image preprocessing
- Extract readable text using EasyOCR
- Display:
  - Original image
  - Processed image
  - Extracted text
- Download extracted text as a `.txt` file

# Image Preprocessing Techniques

The following preprocessing techniques were implemented:
- RGB to Grayscale Conversion
- Gaussian Blur (noise reduction)
- Image enhancement before OCR
These preprocessing steps improve OCR performance by making text clearer and reducing image noise.

# Coding Practice

Separate OCR scripts were created to understand each step individually:
### processing.py
- Reads an image
- Converts it into grayscale
- Applies Gaussian Blur
- Saves processed image

### ocr_engine.py
- Loads EasyOCR
- Reads text from processed image
- Displays extracted text

### save_text.py

- Saves extracted OCR text into a `.txt` file

# Mini Project

## Document OCR Web Application

The Gradio application performs the following tasks:

- Upload document image
- Preprocess image
- Display original image
- Display processed image
- Extract text using EasyOCR
- Show extracted text
- Download extracted text as a TXT file

# Dataset Used

The application was tested on **15+ different document images**, including:

- Printed Documents
- Receipts
- Invoices
- Forms
- Medicine Labels
- Book Pages
- Certificates
- Notes
# How to Run the Project

### Clone Repository

```bash
git clone <repository_link>
```
### Open Project Folder

```bash
cd Day_25
```
### Install Requirements

```bash
pip install -r requirements.txt
```
### Run OCR Practice Scripts

```bash
python "OCR Source Code/processing.py"

python "OCR Source Code/ocr_engine.py"

python "OCR Source Code/save_text.py"
```
### Run Gradio Application

```bash
python app.py
```
After running the application, Gradio will open automatically in your browser.
# Challenges Faced

During this task, I faced several challenges:
- Choosing suitable preprocessing techniques for better OCR accuracy.
- Making the application work with different document types.
- Configuring Gradio correctly with the installed version.
- Generating downloadable text files from OCR output.
- Understanding deployment requirements using ngrok.

# What I Learned

After completing this task, I learned how to:

- Build a complete OCR pipeline.
- Improve OCR accuracy using image preprocessing.
- Integrate EasyOCR with Gradio.
- Extract text from multiple document types.
- Generate downloadable text files.
- Organize an OCR project professionally.

# Possible Improvements

In future versions, I would like to add:
- Multiple language support
- PDF OCR
- Handwritten text recognition
- Batch image processing
- Better image enhancement techniques
- Export OCR results to PDF and Word
- Live camera OCR
