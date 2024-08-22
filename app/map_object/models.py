from app.users.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, ARRAY
from app.users.models import User
import json
import enum
from sqlalchemy import Enum, JSON
from datetime import datetime

from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import FileType

class StatusEnum(enum.Enum):
    new = 'new'
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'    

class Images(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    file = Column(FileType(storage=FileSystemStorage(path="/tmp")))

    def __repr__(self):
        return f'{self.id}: {self.name}'


class Map_Object(Base):
    __tablename__ = "map_object"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    add_time = Column(DateTime)
    user_id = Column(Integer)
    raw_data = Column(JSON)
    images = Column(JSON)
    status = Column('status', Enum(StatusEnum))


