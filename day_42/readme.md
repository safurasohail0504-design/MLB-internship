```markdown
# Day 42 – AI Video Processing API with Background Jobs

## Project Introduction

This project extends the Day 41 YOLO API to support video file processing. The API accepts video uploads, processes them frame-by-frame using YOLO object detection, and returns processed videos with bounding boxes. The system implements background job processing to handle long-running inference tasks without blocking API requests.

## Technologies Used

* FastAPI — Web framework for APIs
* Uvicorn — ASGI server
* YOLO (Ultralytics) — Object detection model
* OpenCV — Video processing and frame handling
* Pydantic — Data validation
* Python 3.11
* UUID — Job ID generation

## Project Structure

```
day_42/
├── app/
│   ├── main.py
│   ├── routes/
│   │   ├── prediction.py (Day 41 - Image)
│   │   └── video.py (Day 42 - Video)
│   ├── services/
│   │   ├── detector.py
│   │   ├── video_processor.py
│   ├── utils/
│   │   └── file_utils.py
│   └── schemas/response.py
├── models/best.pt
├── uploads/ (input videos)
├── outputs/ (processed videos)
├── requirements.txt
└── README.md
```

## What is Video Processing?

Video processing is the application of computer vision algorithms to each frame of a video sequentially. Unlike processing a single image, video processing must handle multiple frames efficiently while maintaining temporal coherence. Each frame is analyzed independently, but the workflow ensures consistent results across all frames.

## What is Background Processing?

Background processing allows the API to accept a video upload, start processing in the background, and immediately return a job ID to the user. The user can then check the processing status without blocking the API. This is essential for long-running tasks because:

- **Non-blocking:** The API remains responsive to other requests
- **Status tracking:** Users can monitor progress without waiting
- **Better UX:** Users get immediate feedback with a job ID instead of waiting for processing to complete
- **Scalable:** Multiple videos can be processed simultaneously

## Job/Status Workflow

The API follows this workflow:

**1. Upload Video**
```
POST /video/process (upload video file)
↓
Returns: job_id, status="processing"
```

**2. Check Status**
```
GET /video/status/{job_id}
↓
Returns: status, progress (0-100), stats
```

**3. Download Result**
```
GET /video/result/{job_id}
↓
Returns: Processed video file (when status="completed")
```

## API Endpoints

**POST /video/process**
- Accepts video file upload (MP4, AVI, MOV)
- Returns job ID and initial status
- Starts background processing task

**GET /video/status/{job_id}**
- Returns current processing status (queued, processing, completed, failed)
- Returns progress percentage (0-100)
- Returns statistics when completed

**GET /video/result/{job_id}**
- Returns processed video file
- Only works when status is "completed"
- Returns 400 error if processing not finished

## How Video Processing Works

1. User uploads video file via POST /video/process
2. API validates file type and size
3. Video is saved to uploads folder with unique job_id
4. Background task starts frame-by-frame processing
5. For each frame:
   - Run YOLO object detection
   - Draw bounding boxes on detected objects
   - Add confidence scores and class names
   - Add frame counter information
6. Processed video is saved to outputs folder
7. Statistics are collected (total frames, detections, FPS, time)
8. Status updates to "completed"
9. User downloads processed video using job_id

## Processing Statistics

Each completed job returns:
- Total Frames: Number of frames in video
- Processed Frames: Number successfully processed
- Total Detections: Total objects detected across all frames
- Average FPS: Frames processed per second
- Processing Time: Total time in seconds

Example output:
```json
{
  "total_frames": 850,
  "processed_frames": 850,
  "total_detections": 1240,
  "average_fps": 18.6,
  "processing_time_seconds": 46.2
}
```

## Error Handling

The API handles:
- Invalid file type (400) — Only MP4, AVI, MOV allowed
- Empty file (400) — File contains no data
- Corrupted video (400/500) — Cannot read frames
- Job not found (404) — Invalid job_id
- Result not found (404) — Processed file missing
- Processing failed (500) — YOLO inference error

## Testing Completed

All endpoints tested using Swagger UI and Postman:

✅ POST /video/process — Video upload and job creation
✅ GET /video/status/{job_id} — Status tracking with progress
✅ GET /video/result/{job_id} — Download processed video
✅ Short video processing (< 1 minute)
✅ Longer video processing (5+ minutes)
✅ Multiple concurrent video uploads
✅ Error handling for invalid file types
✅ Error handling for corrupted videos

## Challenges and Solutions

**Challenge 1: Video codec compatibility**
Solution: Used mp4v codec for output which ensures broad compatibility across platforms and players.

**Challenge 2: Frame numbering and display**
Solution: Added frame counter overlay to each frame so viewers can track progress through the video.

**Challenge 3: Progress tracking during long processing**
Solution: Updated job progress in real-time as frames are processed so users see live progress updates.

**Challenge 4: Memory management for large videos**
Solution: Process frame-by-frame instead of loading entire video into memory.

## Key Features

* Asynchronous video processing with background tasks
* Real-time progress tracking (0-100%)
* Unique job ID for each upload
* YOLO-based object detection on every frame
* Bounding box visualization with labels
* Processing statistics collection
* Temporary file cleanup
* Support for multiple video formats
* Parallel processing capability

## How to Run Locally

```
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Access Swagger UI: `http://127.0.0.1:8000/docs`

