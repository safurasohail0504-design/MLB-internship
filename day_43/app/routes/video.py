from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks, Query
from fastapi.responses import FileResponse
from pathlib import Path
import uuid
import time
from datetime import datetime
from app.services.video_processor import process_video
from app.utils.logger import log_request, log_error, log_warning
from app.utils.file_utils import (
    is_allowed_video, 
    validate_file_size, 
    MAX_VIDEO_SIZE,
    ALLOWED_VIDEO_EXTENSIONS
)
router = APIRouter(prefix="/video", tags=["Video"])
UPLOAD_DIR = Path("uploads")
OUTPUT_DIR = Path("outputs")
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)
jobs = {}
ALLOWED_VIDEO_TYPES = {
    "video/mp4",
    "video/avi",
    "video/x-msvideo",
    "video/mov",
    "video/quicktime"
}
def run_video_processing(job_id: str, input_path: str, output_path: str):
    """Process video in background"""
    try:
        log_request(job_id, "Processing started")
        jobs[job_id]["status"] = "processing"
        jobs[job_id]["start_time"] = datetime.now()
        # Run YOLO inference
        stats = process_video(input_path, output_path, job_id, jobs)
        jobs[job_id]["status"] = "completed"
        jobs[job_id]["progress"] = 100
        jobs[job_id]["stats"] = stats
        jobs[job_id]["end_time"] = datetime.now()
        
        log_request(job_id, f"Processing completed. Detections: {stats['total_detections']}")
    except Exception as e:
        jobs[job_id]["status"] = "failed"
        jobs[job_id]["error"] = str(e)
        jobs[job_id]["end_time"] = datetime.now()
        log_error(job_id, f"Processing failed: {str(e)}")
@router.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "success": True,
        "status": "healthy",
        "model_loaded": True,
        "api_version": "2.0.0",
        "timestamp": datetime.now()
    }
@router.post("/process")
async def process_video_endpoint(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    confidence: float = Query(0.25, ge=0, le=1)
):
    """Upload and process video"""
    job_id = str(uuid.uuid4())
    request_id = f"req_{job_id[:8]}"
    try:
        log_request(request_id, f"Video upload received: {file.filename}")
        # Validation 1: File type
        if not is_allowed_video(file.filename):
            log_warning(request_id, f"Unsupported file type: {file.filename}")
            raise HTTPException(
                status_code=415,
                detail={
                    "success": False,
                    "error": f"Unsupported video format. Allowed: {', '.join(ALLOWED_VIDEO_EXTENSIONS)}",
                    "request_id": request_id
                }
            )
        # Read file
        contents = await file.read()
        # Validation 2: Empty file
        if not contents:
            log_warning(request_id, "Empty file uploaded")
            raise HTTPException(
                status_code=400,
                detail={
                    "success": False,
                    "error": "Uploaded video is empty",
                    "request_id": request_id
                }
            )
        # Validation 3: File size
        is_valid, error_msg = validate_file_size(contents, MAX_VIDEO_SIZE, "Video")
        if not is_valid:
            log_warning(request_id, error_msg)
            raise HTTPException(
                status_code=413,
                detail={
                    "success": False,
                    "error": error_msg,
                    "request_id": request_id
                }
            )
        # Validation 4: Confidence threshold
        if confidence < 0 or confidence > 1:
            log_warning(request_id, f"Invalid confidence: {confidence}")
            raise HTTPException(
                status_code=422,
                detail={
                    "success": False,
                    "error": "Confidence must be between 0 and 1",
                    "request_id": request_id
                }
            )
        # Save file
        filename = file.filename or "uploaded_video.mp4"
        input_path = UPLOAD_DIR / f"{job_id}_{filename}"
        output_path = OUTPUT_DIR / f"{job_id}_processed.mp4"
        with open(input_path, "wb") as buffer:
            buffer.write(contents)
        log_request(request_id, f"File saved: {input_path}")
        # Create job entry
        jobs[job_id] = {
            "job_id": job_id,
            "request_id": request_id,
            "status": "queued",
            "progress": 0,
            "stats": None,
            "error": None,
            "output_path": str(output_path),
            "created_at": datetime.now(),
            "start_time": None,
            "end_time": None
        }
        # Start background processing
        background_tasks.add_task(
            run_video_processing,
            job_id,
            str(input_path),
            str(output_path)
        )
        log_request(request_id, "Job queued for processing")
        return {
            "success": True,
            "job_id": job_id,
            "request_id": request_id,
            "status": "processing",
            "message": "Video queued for processing"
        }
    except HTTPException:
        raise
    except Exception as e:
        log_error(request_id, str(e))
        raise HTTPException(
            status_code=500,
            detail={
                "success": False,
                "error": "Internal server error",
                "request_id": request_id
            }
        )
@router.get("/status/{job_id}")
def get_video_status(job_id: str):
    """Check processing status"""
    request_id = f"req_{job_id[:8]}"
    try:
        if job_id not in jobs:
            log_warning(request_id, f"Job not found: {job_id}")
            raise HTTPException(
                status_code=404,
                detail={
                    "success": False,
                    "error": "Job ID not found",
                    "request_id": request_id
                }
            )
        job = jobs[job_id]
        log_request(request_id, f"Status check - {job['status']}")
        return {
            "success": True,
            "job_id": job_id,
            "request_id": job.get("request_id"),
            "status": job["status"],
            "progress": job["progress"],
            "stats": job["stats"],
            "error": job["error"],
            "timestamp": datetime.now()
        }
    except HTTPException:
        raise
    except Exception as e:
        log_error(request_id, str(e))
        raise HTTPException(status_code=500)
@router.get("/result/{job_id}")
def get_video_result(job_id: str):
    """Download processed video"""
    request_id = f"req_{job_id[:8]}"
    try:
        if job_id not in jobs:
            log_warning(request_id, f"Job not found: {job_id}")
            raise HTTPException(
                status_code=404,
                detail={
                    "success": False,
                    "error": "Job ID not found",
                    "request_id": request_id
                }
            )
        job = jobs[job_id]
        if job["status"] != "completed":
            log_warning(request_id, f"Job not completed. Status: {job['status']}")
            raise HTTPException(
                status_code=400,
                detail={
                    "success": False,
                    "error": f"Processing not completed. Current status: {job['status']}",
                    "request_id": request_id
                }
            )        
        output_path = Path(job["output_path"])
        if not output_path.exists():
            log_error(request_id, f"Output file missing: {output_path}")
            raise HTTPException(
                status_code=404,
                detail={
                    "success": False,
                    "error": "Processed video not found",
                    "request_id": request_id
                }
            )
        log_request(request_id, "Video downloaded")
        return FileResponse(
            path=output_path,
            media_type="video/mp4",
            filename=f"processed_{job_id}.mp4"
        )
    except HTTPException:
        raise
    except Exception as e:
        log_error(request_id, str(e))
        raise HTTPException(status_code=500)