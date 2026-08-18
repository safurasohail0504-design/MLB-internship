from fastapi import APIRouter, HTTPException
from app.schemas.student import Student
router = APIRouter()
students = [
    {
        "id": 1,
        "name": "Ali",
        "age": 21,
        "program": "BSCS"
    },
    {
        "id": 2,
        "name": "Sara",
        "age": 22,
        "program": "BSCS"
    }
]
@router.get("/students")
def get_students():
    return students
@router.post("/students")
def add_student(student: Student):
    new_id = len(students) + 1
    new_student = {
        "id": new_id,
        **student.model_dump()
    }
    students.append(new_student)
    return new_student
@router.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
@router.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    for index, existing_student in enumerate(students):
        if existing_student["id"] == student_id:
            updated_student = {
                "id": student_id,
                **student.model_dump()
            }
            students[index] = updated_student
            return updated_student
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            deleted_student = students.pop(index)
            return {
                "message": "Student deleted successfully",
                "student": deleted_student
            }
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )