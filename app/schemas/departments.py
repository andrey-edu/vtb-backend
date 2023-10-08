from pydantic import BaseModel
from pydantic import Field
from ..schemas import PyObjectId, Coordinates
from enum import Enum
from typing import List, Optional


class Special(BaseModel):
    vipZone: Optional[bool]
    vipOffice: Optional[bool]
    ramp: Optional[bool]
    person: Optional[bool]
    juridical: Optional[bool]
    Prime: Optional[bool]

class Department(BaseModel):
    # id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    id: int
    Biskvit_id: Optional[Optional[str]]
    shortName: Optional[str]
    address: Optional[str]
    city: Optional[str]
    scheduleFl: Optional[str]
    scheduleJurL: Optional[str]
    special: Optional[Special]
    coordinates: Optional[Coordinates]

