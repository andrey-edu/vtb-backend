
from pydantic import BaseModel
from pydantic import Field
from enum import Enum
from typing import List, Optional, Union
from datetime import time


class ClientQuery(BaseModel):
    city: str
    lat: float
    lon: float
    current_time: time


