from fastapi import APIRouter, HTTPException, status
from typing import List
from ..config import vtb


router = APIRouter(
    prefix="/api/cities",
    tags=["Cities"]
)

@router.get("/", response_description="Get list of cities", response_model=List[str])
def get_list_of_cities():
    cities = vtb.departments.distinct( "city" )
    
    if cities is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No cities found"
        )

    return cities
