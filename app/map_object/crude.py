from sqlalchemy.orm import Session
from .models import Map_Object
from .schemas import MapCreate, MapUpdate
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func


def AddData(db: Session, **kwargs):

   try:
      id = db.query(func.max(Map_Object.id)).scalar()
      if id == None:
         id = 1
      else:
         id += 1
      db_map = MapCreate(id=id, title=kwargs['title'], other_titles=kwargs['other_titles'], 
                            connect=kwargs['connect'], add_time=kwargs['add_time'], user=kwargs['user'],
                            coords=str(kwargs['coords']), level=str(kwargs['level']), images=str(kwargs['images']), status='new')

      db.add(db_map)
      db.commit()
      db.refresh(db_map)
      return db_map
   except IntegrityError as e:
      db.rollback()
      print(f'IntegrityError occured: {e.orig}')