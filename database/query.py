from .connect import (engine, 
                    Student,
                    Group,
                    Teacher,
                    AssosiateGroupStudent,
                    AssosiateTeacherGroup)
from sqlalchemy.orm import sessionmaker, Session

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

        if len(groups) != len(group_ids):
            return None

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
        return None
    return student

def add_group_for_student(id: int, gr_id: int):
    db: Session = next(get_db())
    student = db.get(Student, id)
    
    if not student:
        return None
    
    group = db.get(Group, gr_id)

    if group in student.groups:
        return None
    student.groups.append(group)
    db.commit()
    db.refresh(student)
    return student

def update_student(id: int, data: dict):
    db: Session = next(get_db())
    student = db.get(Student, id)
    
    if not student:
        return None
    if "name" in data:
        student.name = data["name"]
    if "year" in data:
        student.year = data["year"]
    if "groups" in data:
        group_ids = data["groups"]
        group_ids = data.get("groups", [])
        groups = db.query(Group).filter(
            Group.id.in_(group_ids)
        ).all()

        if len(groups) != len(group_ids):
           return None

        student.groups = groups
        
    db.commit()
    db.refresh(student)
    return student

def delete_student(id: int):
    db: Session = next(get_db())
    student = db.get(Student, id)

    if not student:
        return None

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