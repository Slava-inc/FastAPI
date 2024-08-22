from pydantic import BaseModel, PydanticUserError
from typing import Optional
from sqlalchemy.types import DateTime
from datetime import datetime
from .models import StatusEnum
from fastapi_storages.integrations.sqlalchemy import FileType
from sqlalchemy.types import LargeBinary

# new record creation schema


class MapCreate(BaseModel):
    id: Optional[int] = 0
    add_time: datetime
    user: int
    raw_data: dict
    images: list[dict] 
    status: StatusEnum 

class ImageCreate(BaseModel):
    id: Optional[int] = 0
    name: str
    file: LargeBinary
	
# read record schema (may be extend later)
# class MapRead(BaseModel):
#     id: int
#     add_time: datetime
#     user: int
#     raw_data: JSON
#     images: JSON 
#     status: StatusEnum 

# update record schema
# class MapUpdate(BaseModel):
#     id: int
#     add_time: datetime
#     user: int
#     raw_data: JSON
#     images: JSON 
#     status: StatusEnum 