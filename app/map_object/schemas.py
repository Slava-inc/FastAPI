from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy.types import DateTime
from datetime import datetime
from .models import StatusEnum
from sqlalchemy import JSON

# new record creation schema


class MapCreate(BaseModel):
    id: Optional[int] = 0
    add_time: datetime
    user: int
    raw_data: JSON
    images: JSON 
    status: StatusEnum   

	
# read record schema (may be extend later)
class MapRead(BaseModel):
    id: int
    add_time: datetime
    user: int
    raw_data: JSON
    images: JSON 
    status: StatusEnum 

# update record schema
class MapUpdate(BaseModel):
    id: int
    add_time: datetime
    user: int
    raw_data: JSON
    images: JSON 
    status: StatusEnum 