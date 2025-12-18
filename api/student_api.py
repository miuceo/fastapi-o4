from typing import List, Optional
from fastapi import APIRouter, status
from fastapi.responses import Response
from fastapi.exceptions import HTTPException
from schemas import (
    StudentBase,
    StudentPatch,
    StudentResponse
)
from database import (
    get_one_student,
    get_all_students,
    create_new_student,
    add_group_for_student,
    update_student,
    delete_student,
    remove_group_for_student
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
    return student

@student_router.post("/", response_model=StudentResponse)
def create_new_student_api(data: StudentBase) :
    student = create_new_student(data.model_dump())
    return student

@student_router.put('/{id}', response_model=StudentResponse)
def put_student_api(id: int, data: StudentBase):
    student = update_student(id, data.model_dump())
    return student

@student_router.patch('/{id}', response_model=StudentResponse)
def patch_student_api(id: int, data: StudentPatch):
    student = update_student(id, data.model_dump(exclude_unset=True))
    return student

@student_router.delete('/{id}')
def delete_student_api(id: int):
    delete_student(id)
    return Response(
        {
            "message": f"Student with id {id} deleted!",
        },
        status_code=status.HTTP_200_OK
    )
    
@student_router.post('/{student_id}/group/{group_id}', response_model=StudentResponse)
def post_new_group_student_api(student_id: int, group_id: int):
    student = add_group_for_student(student_id, group_id)
    return student

@student_router.delete('/{student_id}/group/{group_id}', response_model=StudentResponse)
def delete_group_student_api(student_id: int, group_id: int):
    student = remove_group_for_student(student_id, group_id)
    return student