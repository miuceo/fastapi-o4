from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict

class GroupSimple(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)

class StudentSimple(BaseModel):
    id: int
    name: str
    year: int

    model_config = ConfigDict(from_attributes=True)


class StudentBase(BaseModel):
    name: str = Field(max_length=100, min_length=3)
    year: int
    groups: Optional[List]
    
    model_config = ConfigDict(from_attributes=True)
    
class StudentResponse(BaseModel):
    id: int
    name: str = Field(max_length=100, min_length=3)
    year: int
    groups: Optional[List[GroupSimple]] = None

    model_config = ConfigDict(from_attributes=True)


class StudentPatch(BaseModel):
    name: str | None = None
    year: int | None = None
    groups: Optional[List] | None = None
    
    class Config:
        orm_mode = True
        
