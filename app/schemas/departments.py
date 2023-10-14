from pydantic import BaseModel
from pydantic import Field
from enum import Enum
from typing import List, Optional, Union


class Special(BaseModel):
    vipZone: bool
    vipOffice: bool
    ramp: bool
    person: bool
    juridical: bool
    Prime: bool

class ScheduleDay(BaseModel):
    start: str
    stop: str

class Schedule(BaseModel):
    mon: Optional[Union[ScheduleDay, bool]] = False
    tue: Optional[Union[ScheduleDay, bool]] = False
    wed: Optional[Union[ScheduleDay, bool]] = False
    thu: Optional[Union[ScheduleDay, bool]] = False
    fri: Optional[Union[ScheduleDay, bool]] = False
    sat: Optional[Union[ScheduleDay, bool]] = False
    sun: Optional[Union[ScheduleDay, bool]] = False

class Point(BaseModel):
    type: str
    coordinates: List[float]

class Department(BaseModel):
    id: int
    shortName: str
    address: str
    city: str
    special: Special
    scheduleAllWeekFl: Schedule
    scheduleAllWeekJurl: Schedule
    loc: Point
    current_load: int
    radius_dist: float
