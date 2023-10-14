from fastapi import APIRouter, HTTPException, status
from typing import List
from .. schemas import Department
from ..config import vtb
import json


router = APIRouter(
    prefix="/api/departments",
    tags=["Departments"]
)


@router.get("/all", response_description="Get all departments", response_model=List[Department])
async def get_all_departments():
    cursor = vtb.departments.find( {} )
    departments = await cursor.to_list(None)

    if departments == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There are no departments")
    
    return departments



@router.get("/city/{city}", response_description="Get departments by city", response_model=List[Department])
async def get_departments_by_city(city: str):
    cursor = vtb.departments.find( {"city":city} )
    departments = await cursor.to_list(None)

    if departments == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There are no departments in this city")
    
    return departments