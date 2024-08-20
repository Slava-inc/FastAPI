from app.users.database import Base
from sqlalchemy import Column, Integer, String, DateTime, PickleType
from app.users.models import User
import json
import enum
from sqlalchemy import Enum

class StatusEnum(enum.Enum):
    new = 'new'
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'    



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
    images = Column(PickleType())
    status = Column('status', Enum(StatusEnum))

