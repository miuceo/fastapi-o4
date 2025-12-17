from typing import List, Optional
from fastapi import APIRouter, HTTPException

from database import (
    get_all_groups,
    create_new_group
)
from schemas import (
    GroupBase,
    GroupResponse,
    GroupPatch
)

group_router = APIRouter(
    prefix='/groups'
)

@group_router.get("/", response_model=List[GroupResponse])
def get_all_groups_api():
    return get_all_groups()

@group_router.post("/", response_model=GroupResponse)
def create_new_group_api(data: GroupBase):
    group = create_new_group(data.model_dump())
    if group:
        return group
    else:
        raise HTTPException(400, "Cannot create group!")