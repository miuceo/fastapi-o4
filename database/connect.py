from typing import List

from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship
)


class Base(DeclarativeBase):
    pass

class AssosiateTeacherGroup(Base):
    __tablename__ = "assosiate_tg"
    teacher_id: Mapped[int] = mapped_column(ForeignKey('teacher.id', ondelete='CASCADE'), primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey('group.id', ondelete='CASCADE'), primary_key=True)

    def __repr__(self,):
        return f'{self.teacher_id} - {self.group_id}'


class AssosiateGroupStudent(Base):
    __tablename__ = "assosiate_sg"
    student_id: Mapped[int] = mapped_column(ForeignKey('student.id', ondelete='CASCADE'), primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey('group.id', ondelete='CASCADE'), primary_key=True)


    def __repr__(self,):
        return f'{self.student_id} - {self.group_id}'


class Teacher(Base):
    __tablename__ = 'teacher'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    year: Mapped[int]
    groups: Mapped[List['Group']] = relationship(
        secondary="assosiate_tg",
        back_populates='teachers'
    )

    def __repr__(self,):
        return self.name


class Group(Base):
    __tablename__ = 'group'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    teachers: Mapped[List['Teacher']] = relationship(
        secondary="assosiate_tg",
        back_populates="groups" 
    )
    students: Mapped[List['Student']] = relationship(
        secondary="assosiate_sg",
        back_populates="groups"
    )

    def __repr__(self,):
        return self.name

class Student(Base):
    __tablename__ = 'student'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    year: Mapped[int]

    groups: Mapped[List['Group']] = relationship(
        secondary="assosiate_sg",
        back_populates='students'
    )

    def __repr__(self):
        return self.name


engine = create_engine("postgresql+psycopg2://postgres:197346825Miu@127.0.0.1:5432/example_db")
Base.metadata.create_all(engine)