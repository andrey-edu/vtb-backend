from fastapi import APIRouter, HTTPException, status
from typing import List
from .. schemas import Department, ClientQuery
from ..config import vtb
import json
from ..utils import get_random_load
from geopy import distance


router = APIRouter(
    prefix="/api/departments",
    tags=["Departments"]
)


@router.post("/all", response_description="Get all departments", response_model=List[Department])
async def get_all_departments(data: ClientQuery):

    initialLocation = (data.lat, data.lon)

    cursor = vtb.departments.find( {} )
    departments = await cursor.to_list(1)

    if departments == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There are no departments")


    for department in departments:

        # Узнаем текущую нагруженность отделения
        department["current_load"] = get_random_load()

        # Вычисляем расстояние до отделения по прямой
        depLocation = (
            department["loc"]["coordinates"][1],
            department["loc"]["coordinates"][0]
        )
        department["radius_dist"] = distance.distance(initialLocation, depLocation).km
    
    return departments



@router.post("/city", response_description="Get departments by city", response_model=List[Department])
async def get_departments_by_city(data: ClientQuery):

    initialLocation = (data.lat, data.lon)

    cursor = vtb.departments.find( {"city":data.city} )
    departments = await cursor.to_list(None)

    if departments == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There are no departments in this city")
    

    for department in departments:

        # Узнаем текущую нагруженность отделения
        department["current_load"] = get_random_load()

        # Вычисляем расстояние до отделения по прямой
        depLocation = (
            department["loc"]["coordinates"][1],
            department["loc"]["coordinates"][0]
        )
        department["radius_dist"] = distance.distance(initialLocation, depLocation).km
    
    
    return departments