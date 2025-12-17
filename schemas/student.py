from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict

class StudentBase(BaseModel):
    name: str = Field(max_length=100, min_length=3)
    year: int
    groups: List[Optional[int]] | None
    
class StudentResponce(BaseModel):
    id: int
    name: str = Field(max_length=100, min_length=3)
    year: int
    groups: List

class StudentPatch(BaseModel):
    name: str | None = None
    year: int | None = None
    groups: List | None = None