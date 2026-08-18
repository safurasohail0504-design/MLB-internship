from fastapi import FastAPI
from app.routes.students import router as students_router

app = FastAPI(
    title="Student Management API",
    description="A simple Student Management REST API built with FastAPI",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Student Management API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


app.include_router(students_router)