from fastapi import APIRouter, HTTPException
from schemas import (
    StudentBase
)
from database import (
    get_one_student,
    get_all_students,
    create_new_student
)

student_router = APIRouter(
    prefix='/students',
)

@student_router.get("/")
def get_all_students_api():
    return get_all_students()

@student_router.get("/{id}")
def get_all_students_api(id: int):
    return get_one_student(id)

@student_router.post("/")
def create_new_student_api(data: StudentBase):
    return create_new_student(data.model_dump())