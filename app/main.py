from fastapi import FastAPI
from .routers import cities, departments

app = FastAPI(
    title = "VTB Departments",
    docs_url = "/documentation",
    redoc_url = None
)

app.include_router(cities.router)
app.include_router(departments.router)
