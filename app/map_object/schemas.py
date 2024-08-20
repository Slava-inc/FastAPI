from pydantic import BaseModel, Field
from typing import Optional
from app.users.models import User
from sqlalchemy.types import DateTime

# new record creation schema
class MapCreate(BaseModel):
    title: str
    other_titles: str
    connect: str
    add_time: DateTime
    user: User
    coords = {'latitude': float, 'longitude': float, 'height': int}
    level = {'winter': str, 'summer': str, 'autumn':str, 'spring': str}
    images = [{'data':bytes}]    

	
# read record schema (may be extend later)
class MapRead(BaseModel):
    id: int
    title: str
    other_titles: str
    connect: str
    add_time: DateTime
    user: User
    coords = {'latitude': float, 'longitude': float, 'height': int}
    level = {'winter': str, 'summer': str, 'autumn':str, 'spring': str}
    images = [{'data':bytes}]

# update record schema
class MapUpdate(BaseModel):
    id: int
    title: str
    other_titles: str
    connect: str
    add_time: DateTime
    user: User
    coords = {'latitude': float, 'longitude': float, 'height': int}
    level = {'winter': str, 'summer': str, 'autumn':str, 'spring': str}
    images = [{'data':bytes}]