from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from pathlib import Path
import uuid

from app.services.video_processor import process_video


router = APIRouter(
    prefix="/video",
    tags=["Video"]
)


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


def run_video_processing(
    job_id: str,
    input_path: str,
    output_path: str
):

    try:

        jobs[job_id]["status"] = "processing"

        stats = process_video(
            input_path,
            output_path,
            job_id,
            jobs
        )

        jobs[job_id]["status"] = "completed"
        jobs[job_id]["progress"] = 100
        jobs[job_id]["stats"] = stats

    except Exception as e:

        jobs[job_id]["status"] = "failed"
        jobs[job_id]["error"] = str(e)


@router.post("/process")
async def process_video_endpoint(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...)
):

    if file.content_type not in ALLOWED_VIDEO_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only MP4, AVI and MOV videos are allowed."
        )

    contents = await file.read()

    if not contents:
        raise HTTPException(
            status_code=400,
            detail="Uploaded video is empty."
        )

    job_id = str(uuid.uuid4())

    filename = file.filename or "uploaded_video.mp4"

    input_path = UPLOAD_DIR / f"{job_id}_{filename}"

    output_path = OUTPUT_DIR / f"{job_id}_processed.mp4"

    with open(input_path, "wb") as buffer:
        buffer.write(contents)

    jobs[job_id] = {
        "job_id": job_id,
        "status": "queued",
        "progress": 0,
        "stats": None,
        "error": None,
        "output_path": str(output_path)
    }

    background_tasks.add_task(
        run_video_processing,
        job_id,
        str(input_path),
        str(output_path)
    )

    return {
        "job_id": job_id,
        "status": "processing"
    }


@router.get("/status/{job_id}")
def get_video_status(job_id: str):

    if job_id not in jobs:
        raise HTTPException(
            status_code=404,
            detail="Job ID not found."
        )

    job = jobs[job_id]

    return {
        "job_id": job_id,
        "status": job["status"],
        "progress": job["progress"],
        "stats": job["stats"],
        "error": job["error"]
    }


@router.get("/result/{job_id}")
def get_video_result(job_id: str):

    if job_id not in jobs:
        raise HTTPException(
            status_code=404,
            detail="Job ID not found."
        )

    job = jobs[job_id]

    if job["status"] != "completed":
        raise HTTPException(
            status_code=400,
            detail="Video processing is not completed yet."
        )

    output_path = Path(job["output_path"])

    if not output_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Processed video not found."
        )

    return FileResponse(
        path=output_path,
        media_type="video/mp4",
        filename=f"processed_{job_id}.mp4"
    )