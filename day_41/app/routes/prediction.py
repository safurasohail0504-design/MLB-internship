from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import tempfile
import os
import cv2
from app.services.detector import predict_image, model
router = APIRouter()
ALLOWED_TYPES = {
    "image/jpeg",
    "image/png",
    "image/jpg"
}
def validate_upload(file: UploadFile, contents: bytes, confidence: float):
    # Check file type
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only JPG, JPEG and PNG images are allowed."
        )
    # Check empty file
    if not contents:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty."
        )
    # Check confidence
    if confidence < 0 or confidence > 1:
        raise HTTPException(
            status_code=400,
            detail="Confidence must be between 0 and 1."
        )
# HEALTH CHECK
@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }
# JSON PREDICTION
@router.post("/predict")
async def predict(
    file: UploadFile = File(...),
    confidence: float = 0.25
):
    contents = await file.read()
    validate_upload(
        file,
        contents,
        confidence
    )
    suffix = Path(file.filename).suffix or ".jpg"
    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as temp_file:
            temp_file.write(contents)
            temp_path = temp_file.name
        # YOLO prediction
        detections = predict_image(
            temp_path,
            confidence
        )
        return {
            "detections": detections,
            "total": len(detections)
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"YOLO inference failed: {str(e)}"
        )
    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)
# PREDICTION + PROCESSED IMAGE
@router.post("/predict/image")
async def predict_image_with_boxes(
    file: UploadFile = File(...),
    confidence: float = 0.25
):
    contents = await file.read()
    validate_upload(
        file,
        contents,
        confidence
    )
    suffix = Path(file.filename).suffix or ".jpg"
    temp_input = None
    output_path = None
    try:
        # Save uploaded image temporarily
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as temp_file:
            temp_file.write(contents)
            temp_input = temp_file.name
        # YOLO INFERENCE
        results = model.predict(
            temp_input,
            conf=confidence,
            verbose=False
        )
        # READ IMAGE
        img = cv2.imread(temp_input)
        if img is None:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is not a valid image."
            )
        # DRAW BOUNDING BOXES
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0].tolist()
                )
                class_id = int(box.cls[0])
                class_name = result.names[class_id]
                confidence_value = float(
                    box.conf[0]
                )
                # Bounding box
                cv2.rectangle(
                    img,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )
                # Label
                label = (
                    f"{class_name} "
                    f"{confidence_value:.2f}"
                )
                cv2.putText(
                    img,
                    label,
                    (x1, max(y1 - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )
        # SAVE PROCESSED IMAGE
        output_path = tempfile.NamedTemporaryFile(
            delete=False,
            suffix="_prediction.jpg"
        ).name
        cv2.imwrite(
            output_path,
            img
        )
        # RETURN IMAGE
        return FileResponse(
            output_path,
            media_type="image/jpeg",
            filename="prediction.jpg"
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"YOLO inference failed: {str(e)}"
        )
    finally:
        # Remove input temporary file.
        # Output file is left temporarily so
        # FileResponse can send it.
        if temp_input and os.path.exists(temp_input):

            os.remove(temp_input)