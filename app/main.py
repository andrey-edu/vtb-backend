from fastapi import FastAPI
from .routers import cities

app = FastAPI(
    title = "VTB Departments",
    docs_url = None,
    redoc_url = None
)

app.include_router(cities.router)
