from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy.types import DateTime
from datetime import datetime
from .models import StatusEnum

# new record creation schema


class MapCreate(BaseModel):
    title: str
    other_titles: str
    connect: str
    add_time: datetime
    user: int
    coords: str
    level: str
    images: str 
    status: StatusEnum   

	
# read record schema (may be extend later)
class MapRead(BaseModel):
    id: int
    title: str
    other_titles: str
    connect: str
    add_time: datetime
    user: int
    coords: str
    level: str
    images: str
    status: StatusEnum

# update record schema
class MapUpdate(BaseModel):
    id: int
    title: str
    other_titles: str
    connect: str
    add_time: datetime
    user: int
    coords: str
    level: str
    images: str
    status: StatusEnum