from typing import List, Optional
from fastapi import APIRouter, HTTPException

from database import (
    get_all_groups,
    create_new_group,
    get_single_group,
    update_group
)
from schemas import (
    GroupBase,
    GroupResponse,
    GroupPatch,
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
    
@group_router.get('/{id}', response_model=GroupResponse)
def get_single_group_api(id: int):
    group = get_single_group(id)
    return group

@group_router.put('/{id}', response_model=GroupResponse)
def put_group_api(id: int, data: GroupBase):
    group = update_group(id, data.model_dump())
    return group

@group_router.patch('/{id}', response_model=GroupResponse)
def patch_group_api(id: int, data: GroupPatch):
    group = update_group(id, data.model_dump(exclude_unset=True))
    return group

