from fastapi import FastAPI
from app.routes.prediction import router as prediction_router
app = FastAPI(
    title="Custom YOLO Prediction API",
    description="FastAPI backend for custom YOLO object detection",
    version="1.0.0"
)
@app.get("/")
def root():
    return {
        "message": "Welcome to Custom YOLO Prediction API"
    }
app.include_router(prediction_router)