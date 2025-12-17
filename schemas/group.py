from typing import Optional, List

from pydantic import BaseModel, ConfigDict, Field
from .student import StudentBase, StudentSimple

class GroupBase(BaseModel):
    name: str = Field(max_length=50, min_length=3)
    teachers: Optional[List]
    students: Optional[List]
    
    model_config = ConfigDict(from_attributes=True)
    
class GroupResponse(BaseModel):
    id: int
    name: str = Field(max_length=50, min_length=3)
    students: Optional[List[StudentSimple]] = None

    model_config = ConfigDict(from_attributes=True)
    
class GroupPatch(BaseModel):
    name: str | None = None
    teachers: Optional[List] | None = None
    students: Optional[List] | None = None
    
    class Config:
        orm_mode = True