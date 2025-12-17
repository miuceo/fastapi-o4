from typing import List, Optional
from fastapi import APIRouter, HTTPException
from schemas import (
    StudentBase,
    StudentPatch,
    StudentResponse
)
from database import (
    get_one_student,
    get_all_students,
    create_new_student,
    add_group_for_student
)

student_router = APIRouter(
    prefix='/students',
)

@student_router.get("/", response_model=List[StudentResponse])
def get_all_students_api():
    return get_all_students()

@student_router.get("/{id}", response_model=StudentResponse)
def get_all_students_api(id: int):
    student = get_one_student(id)
    if not student:
        raise HTTPException(404, f"Student with id {id} not found")
    return student

@student_router.post("/", response_model=StudentResponse)
def create_new_student_api(data: StudentBase) :
    student = create_new_student(data.model_dump())
    if not student:
        raise HTTPException(501, "Some groups don't exists!")
    return student

@student_router.post('/{student_id}/group/{group_id}', response_model=StudentResponse)
def post_new_group(student_id: int, group_id: int):
    student = add_group_for_student(student_id, group_id)
    if not student:
        raise HTTPException(404, "Student or group doesn't exists or already in database!")
    return student
