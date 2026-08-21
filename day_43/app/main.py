from fastapi import FastAPI
from app.routes.prediction import router as prediction_router
from app.routes.video import router as video_router
app = FastAPI(
    title="Custom YOLO AI API",
    description="FastAPI backend for YOLO image and video processing",
    version="2.0.0"
)
@app.get("/")
def root():
    return {
        "message": "Welcome to Custom YOLO AI API"
    }
# Day 41 image prediction routes
app.include_router(prediction_router)
# Day 42 video processing routes
app.include_router(video_router)