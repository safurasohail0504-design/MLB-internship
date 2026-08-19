from pydantic import BaseModel, Field
from typing import List
class Detection(BaseModel):
    class_name: str = Field(alias="class")
    confidence: float
    bbox: List[float]
    class Config:
        populate_by_name = True
class PredictionResponse(BaseModel):
    detections: List[Detection]
    total: int