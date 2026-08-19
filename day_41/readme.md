# Day 41 – Custom YOLO Prediction API

## Project Introduction

This project integrates a custom YOLO shoe detection model with FastAPI to create a production-ready REST API. The API accepts image uploads, runs YOLO inference, and returns predictions in JSON format with bounding box coordinates and confidence scores.

## Technologies Used

* FastAPI — Web framework for building APIs
* Uvicorn — ASGI server
* YOLO (Ultralytics) — Object detection model
* OpenCV — Image processing
* Pydantic — Data validation
* Python 3.11

## Project Structure
day_41/
├── app/
│ ├── main.py
│ ├── routes/prediction.py
│ ├── services/detector.py
│ └── schemas/response.py
├── models/best.pt
├── requirements.txt
└── README.md

## API Endpoints

**GET /health**
- Confirms API is running and model is loaded
- Returns status and model_loaded flag

**GET /**
- Welcome message
- Returns API introduction

**POST /predict**
- Accepts image file (JPG, PNG, JPEG)
- Runs YOLO inference
- Returns JSON with detections array containing class name, confidence, and bounding box coordinates
- Query parameter: confidence (0.0-1.0, default 0.25)

**POST /predict/image**
- Accepts image file (JPG, PNG, JPEG)
- Runs YOLO inference and draws bounding boxes on image
- Returns processed image with labels and confidence scores
- Query parameter: confidence (0.0-1.0, default 0.25)

## How FastAPI Connects with YOLO

FastAPI receives HTTP requests with image uploads. The image is temporarily saved and passed to the YOLO model for inference. The model detects objects and returns predictions. FastAPI formats these predictions as JSON and returns them to the client.

## Request and Response Format

**POST /predict Request**
File: image.jpg
confidence: 0.25 (optional)

**POST /predict Response (200 OK)**
```json
{
  "detections": [
    {
      "class": "shoe",
      "confidence": 0.91,
      "bbox": [120.5, 80.2, 340.8, 420.1]
    },
    {
      "class": "shoe",
      "confidence": 0.87,
      "bbox": [350.1, 90.5, 520.3, 450.2]
    }
  ],
  "total": 2
}
```

## Error Handling

**400 Bad Request**
- Unsupported file type (not JPG, PNG, JPEG)
- Empty file uploaded
- Invalid confidence value (not between 0 and 1)

**422 Unprocessable Entity**
- Missing required file parameter

**500 Internal Server Error**
- YOLO inference failed
- Model loading error

## Testing

All endpoints were tested using Swagger UI at `/docs`:

✅ GET /health — Model loaded status confirmed
✅ POST /predict with valid shoe image — Detections returned correctly
✅ POST /predict with confidence 0.25 — All detections included
✅ POST /predict with confidence 0.75 — Fewer detections (high threshold)
✅ POST /predict with unsupported file type — 400 error returned
✅ POST /predict with empty file — 400 error returned
✅ POST /predict with no objects in image — Total: 0 returned
✅ POST /predict/image — Processed image with bounding boxes returned

**Testing Note:** Thunder Client was used for GET /health testing only. File upload testing (POST endpoints) was performed exclusively with Swagger UI, as Thunder Client's file upload feature is only available in the paid version.

## How to Run Locally

1. Install dependencies:
pip install -r requirements.txt

2. Start the server:
python -m uvicorn app.main:app --reload

3. Access API:http://127.0.0.1:8000/docs


## Model Information

**Model:** best.pt (custom YOLO model)
**Trained on:** Shoe detection dataset
**Classes:** Shoe
**Input:** Images (JPG, PNG, JPEG)
**Output:** Bounding box coordinates, class name, confidence score

## Key Features

* Image validation before processing
* Confidence threshold adjustment
* Temporary file handling
* Automatic cleanup of temp files
* JSON response formatting
* Bounding box drawing with OpenCV
* Error messages with HTTP status codes
* Interactive Swagger documentation

## Deployment

Deployed on Render at: `https://fastapi-day41.onrender.com/docs`

## What I Learned

* How FastAPI integrates with ML models
* File upload handling in FastAPI
* Image processing with OpenCV
* Pydantic data validation
* Proper error handling and HTTP status codes
* Building production-ready APIs
* Swagger/OpenAPI documentation