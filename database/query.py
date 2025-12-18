from .connect import (engine, 
                    Student,
                    Group,
                    Teacher,
                    AssosiateGroupStudent,
                    AssosiateTeacherGroup)
from sqlalchemy.orm import sessionmaker, Session
from fastapi import status
from fastapi.exceptions import HTTPException

SessionLocal = sessionmaker(bind=engine,
                       autoflush=False,
                       autocommit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
# Student

def create_new_student(data: dict):
    db: Session = next(get_db())

    group_ids = data.get("groups", [])

    student = Student(
        name=data["name"],
        year=data["year"],
        groups=[]
    )

    if group_ids:
        groups = db.query(Group).filter(
            Group.id.in_(group_ids)
        ).all()

        student.groups.extend(groups)

    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def get_all_students():
    db: Session = next(get_db())
    
    students = db.query(Student).all()
    
    return students

def get_one_student(id: int):
    db: Session = next(get_db())
    
    student = db.get(Student, id)
    
    if not student:
        raise HTTPException(status_code=404, detail=f"Student with id {id} not found!")
    
    return student

def add_group_for_student(id: int, gr_id: int):
    db: Session = next(get_db())
    student = db.get(Student, id)
    
    if not student:
        raise HTTPException(status_code=404, detail=f"Student with id {id} not found!")
    
    group = db.get(Group, gr_id)

    if not group:
        raise HTTPException(
            status_code=404,
            detail=f"Group with id {gr_id} not found!"
        )
        
    if group in student.groups:
        raise HTTPException(
            status_code=400,
            detail=f"Student already belongs to group {gr_id}!"
        )

    student.groups.append(group)
    db.commit()
    db.refresh(student)
    return student

def remove_group_for_student(id: int, gr_id: int):
    db: Session = next(get_db())
    student = db.get(Student, id)
    
    if not student:
        raise HTTPException(status_code=404, detail=f"Student with id {id} not found!")
    
    group = db.get(Group, gr_id)

    if not group:
        raise HTTPException(404, f"Group with id {gr_id} not found!")

    if group not in student.groups:
        raise HTTPException(400, f"Student is not in group {gr_id}!")

        
    student.groups.remove(group)
    db.commit()
    db.refresh(student)
    return student

def update_student(id: int, data: dict):
    db: Session = next(get_db())
    student = db.get(Student, id)

    
    if not student:
        raise HTTPException(status_code=404, detail=f"Student with id {id} not found!")
    
    if "name" in data:
        student.name = data["name"]
    if "year" in data:
        student.year = data["year"]
    if "groups" in data:
        group_ids = data.get("groups", [])
        groups = db.query(Group).filter(
            Group.id.in_(group_ids)
        ).all()

        student.groups = groups
        
    db.commit()
    db.refresh(student)
    return student

def delete_student(id: int):
    db: Session = next(get_db())
    student = db.get(Student, id)

    if not student:
        raise HTTPException(status_code=404, detail=f"Student with id {id} not found!")

    db.delete(student)
    db.commit()
    return True

# Course

def get_all_groups():
    
    db: Session = next(get_db())
    
    groups = db.query(Group).all()
    
    return groups

def create_new_group(data):
    db: Session = next(get_db())
    group = Group(**data)
    db.add(group)
    db.commit()
    db.refresh(group)
    return group

def get_single_group(id: int):
    db: Session = next(get_db())
    
    group = db.get(Group, id)
    
    if not group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Group with id {id} not found!")
    
    return group

def update_group(id: int, data: dict):
    db: Session = next(get_db())
    group = db.get(Group, id)
    
    if not group:
        raise HTTPException(status_code=404, detail=f"Group with id {id} not found!")
    
    if "name" in data:
        group.name = data["name"]
    if "students" in data:
        student_ids = data.get("students", [])
        students = db.query(Student).filter(
            Student.id.in_(student_ids)
        ).all()

        group.students = students
        
    if "teachers" in data:
        teachers_ids = data.get("teachers", [])
        teachers = db.query(Teacher).filter(
            Teacher.id.in_(teachers_ids)
        ).all()

        group.teachers = teachers
        
    db.commit()
    db.refresh(group)
    return group