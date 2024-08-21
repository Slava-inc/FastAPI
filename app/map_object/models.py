from app.users.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, ARRAY
from app.users.models import User
import json
import enum
from sqlalchemy import Enum
from sqlalchemy.orm import  relationship

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
    title = Column(String, index=True, unique=True)
    other_titles = Column(String, index=True, unique=False)
    connect = Column(String)
    add_time = Column(DateTime)
    user = Column(Integer)
    coords = Column(String)
    level = Column(String)
    images = Column(ARRAY(String, ForeignKey("Images.id")))
    status = Column('status', Enum(StatusEnum))

