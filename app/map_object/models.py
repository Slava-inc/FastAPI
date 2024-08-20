from app.users.database import Base
from sqlalchemy import Column, Integer, String, DateTime, PickleType
from app.users.models import User

class Map_Object(Base):
    __tablename__ = "map_object"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True, unique=True)
    other_titles = Column(String, index=True, unique=False)
    connect = Column(String)
    add_time = Column(DateTime)
    user = Column(User)
    coords = Column(PickleType)
    level = Column(PickleType)
    images = Column(PickleType)
