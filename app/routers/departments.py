from fastapi import APIRouter, HTTPException, status
# from .. import schemas
# from typing import List
from ..config import departments_collection
import json


router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)

@router.post("/", response_description="Get all departments by city", response_model=StudentModel)


@router.get("/{pk}", response_model=schemas.Article)
def get_article(pk: str):

    title = redis_db.hget(pk, "title")
    abstract = redis_db.hget(pk, "abstract")
    paragraphs = redis_db.hget(pk, "article")

    if paragraphs is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no such article yet")

    article = schemas.Article(
        title = title,
        abstract = abstract,
        paragraphs = json.loads(paragraphs)
    )

    return article