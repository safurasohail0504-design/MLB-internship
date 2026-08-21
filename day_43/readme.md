# Day 43 – Production-Ready AI API with Validation & Logging

## Project Introduction

This project extends the Day 42 YOLO video processing API to be production-ready by adding comprehensive validation, error handling, and logging. The API now validates all inputs, returns meaningful error responses, logs all events, and gracefully handles edge cases instead of crashing when users provide bad input.

## Technologies Used

* FastAPI — Web framework for APIs
* Uvicorn — ASGI server
* YOLO (Ultralytics) — Object detection model
* OpenCV — Video processing and frame handling
* Python logging — Event tracking and debugging
* Python 3.11
* UUID — Unique request/job ID generation

## Project Structure
day_43/
├── app/
│ ├── main.py
│ ├── routes/
│ │ ├── prediction.py (Day 41 - Image)
│ │ └── video.py 
│ ├── services/
│ │ ├── detector.py
│ │ ├── video_processor.py
│ ├── utils/
│ │ ├── logger.py 
│ │ └── file_utils.py 
│ └── schemas/response.py
├── models/best.pt
├── logs/ app.log
├── requirements.txt
└── README.md


## What is API Validation?

API validation ensures that incoming requests meet requirements before processing. Instead of assuming users will send correct data, production APIs validate:

- **File types** — Is it a supported format?
- **File sizes** — Is it within limits?
- **Parameters** — Are confidence values between 0-1?
- **Request structure** — Are required fields present?

## What is Error Handling?

Error handling ensures the API returns meaningful responses instead of crashing. Production APIs:

- **Catch exceptions** — Don't let errors cascade
- **Return appropriate HTTP status codes** — 400, 404, 413, 422, 500
- **Provide error details** — Tell users what went wrong
- **Include request_id** — Help users track their requests

## What is Logging?

Logging tracks what happens in the API for debugging and monitoring:

- **INFO** — Important events (upload received, processing started)
- **WARNING** — Something unexpected (unsupported file type)
- **ERROR** — Something failed (processing crashed)

Each log entry includes timestamp and request_id for tracing.

## Validations Implemented

### 1. File Type Validation

**Allowed formats:** MP4, AVI, MOV, MKV

**Error code:** 415 Unsupported Media Type

```json
{
  "success": false,
  "error": "Unsupported video format. Allowed: .mp4, .avi, .mov, .mkv",
  "request_id": "req_abc123"
}
```

### 2. File Size Validation

**Maximum size:** 500MB for videos

**Error code:** 413 Payload Too Large

```json
{
  "success": false,
  "error": "Video exceeds 500MB limit. Uploaded: 650.25MB",
  "request_id": "req_abc123"
}
```

### 3. Confidence Threshold Validation

**Valid range:** 0.0 to 1.0

**Error code:** 422 Unprocessable Entity

```json
{
  "success": false,
  "error": "Confidence must be between 0 and 1",
  "request_id": "req_abc123"
}
```

### 4. Empty File Validation

**Rejects:** Files with zero bytes

**Error code:** 400 Bad Request

```json
{
  "success": false,
  "error": "Uploaded video is empty",
  "request_id": "req_abc123"
}
```

### 5. Job ID Validation

**Rejects:** Non-existent job IDs

**Error code:** 404 Not Found

```json
{
  "success": false,
  "error": "Job ID not found",
  "request_id": "req_abc123"
}
```

## HTTP Status Codes Used

| Code | Meaning | Example |
|------|---------|---------|
| **200** | Success | Video upload accepted, status retrieved |
| **400** | Bad Request | Empty file, invalid confidence |
| **404** | Not Found | Job ID not found, result file missing |
| **413** | Payload Too Large | Video exceeds size limit |
| **415** | Unsupported Type | Unsupported file format |
| **422** | Unprocessable | Invalid parameter values |
| **500** | Server Error | YOLO inference failed |

## Logging System

### Log Levels

**INFO** — Normal operation events
INFO - [req_abc123] Video upload received: video.mp4
INFO - [req_abc123] File saved: uploads/job_xyz_video.mp4
INFO - [req_abc123] Job queued for processing
INFO - [req_abc123] Processing started
INFO - [req_abc123] Processing completed. Detections: 45

**WARNING** — Unexpected but handled situations
WARNING - [req_abc123] Unsupported file type: file.txt
WARNING - [req_abc123] Job not completed. Status: processing

**ERROR** — Failures that need attention
ERROR - [req_abc123] Processing failed: Video codec not supported
ERROR - [req_abc123] YOLO inference crashed: Out of memory

### Log File Location

`logs/app.log` — Created automatically, contains all events

## API Endpoints

### GET /health

Returns API and model status.

**Response (200 OK):**
```json
{
  "success": true,
  "status": "healthy",
  "model_loaded": true,
  "api_version": "2.0.0",
  "timestamp": "2026-08-20T18:00:00"
}
```

### POST /video/process

Upload and start video processing.

**Validations:**
- ✅ File type (MP4, AVI, MOV, MKV only)
- ✅ File size (max 500MB)
- ✅ Confidence (0.0-1.0)
- ✅ File not empty

**Success Response (200):**
```json
{
  "success": true,
  "job_id": "550e8400-e29b-41d4-a716-446655440000",
  "request_id": "req_550e8400",
  "status": "processing",
  "message": "Video queued for processing"
}
```

### GET /video/status/{job_id}

Check processing progress.

**Success Response (200):**
```json
{
  "success": true,
  "job_id": "550e8400-e29b-41d4-a716-446655440000",
  "request_id": "req_550e8400",
  "status": "processing",
  "progress": 45,
  "stats": null,
  "timestamp": "2026-08-20T18:01:00"
}
```

### GET /video/result/{job_id}

Download processed video (only when status="completed").

**Success Response (200):** Downloads MP4 file

**Error Response (400):** Not completed yet

## Testing Completed

### Validation Tests (Error Cases)

✅ Unsupported file type (.txt) → 415 error
✅ Confidence too low (-0.5) → 422 error
✅ Confidence too high (1.5) → 422 error
✅ Invalid job ID → 404 error
✅ Download before completion → 400 error
✅ Empty file upload → 400 error

### Success Tests

✅ Valid video upload → 200 with job_id
✅ Check status during processing → 200 with progress
✅ Health check → 200 with model status
✅ Download after completion → 200 with video file

### Logging Tests

✅ All events logged to `logs/app.log`
✅ Request IDs tracked throughout workflow
✅ Errors logged with context
✅ Processing times recorded

## Key Features

* **Request validation** — Type, size, parameter checks
* **Error handling** — Graceful failures, meaningful messages
* **Structured logging** — Track all events in logs/app.log
* **Request tracking** — Unique request_id for each operation
* **HTTP status codes** — Proper codes for each error type
* **Health endpoint** — Monitor API and model status
* **Timestamps** — Know when events occurred
* **Background processing** — Long tasks don't block API

## How to Run Locally
pip install -r requirements.txt
python -m uvicorn app.main:app --reload

Access Swagger UI: `http://127.0.0.1:8000/docs`

View logs: `cat logs/app.log`

## Challenges Faced

**Challenge 1: Validation timing**
Solution: Validate early before any processing starts to save resources.

**Challenge 2: Meaningful error messages**
Solution: Include specific details (file size, confidence range) in errors.

**Challenge 3: Request tracking**
Solution: Generate unique request_id at start, include in all logs and responses.

**Challenge 4: Logging performance**
Solution: Write to file asynchronously so logging doesn't slow API.

## Production Readiness Checklist

✅ Input validation on all endpoints
✅ Proper HTTP status codes
✅ Meaningful error messages
✅ Logging system in place
✅ Request tracking (request_id)
✅ Health check endpoint
✅ Graceful error handling
✅ No crashes on bad input
✅ Timestamps on all events
✅ File size limits enforced

## What I Learned

* API validation prevents bad data from reaching processing
* Error handling makes APIs reliable and user-friendly
* Logging is essential for debugging production issues
* HTTP status codes tell clients what went wrong
* Request IDs help trace issues across logs
* Production APIs must handle user mistakes gracefully

## Next Steps

Day 44 will add **database integration** to store:
- User accounts
- Processing history
- Job results
- Statistics