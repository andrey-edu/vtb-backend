from pydantic import BaseModel
from pydantic import Field
from ..schemas import PyObjectId, Coordinates
from enum import Enum
from typing import List, Optional


class Special(BaseModel):
    vipZone: bool
    vipOffice: bool
    ramp: bool
    person: bool
    juridical: bool
    Prime: bool

class Department(BaseModel):
    # id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    id: int
    Biskvit_id: str
    shortName: str
    address: str
    city: str
    scheduleFl: str
    scheduleJurL: str
    special: Special
    coordinates: Coordinates

