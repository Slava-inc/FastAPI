from sqlalchemy.orm import Session
from .models import Map_Object
from .schemas import MapCreate, MapUpdate
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func


def submitData(db: Session, **kwargs):

   try:
      id = db.query(func.max(Map_Object.id)).scalar()
      if id == None:
         id = 1
      else:
         id += 1
      db_map = Map_Object(id=id, title=kwargs.title, other_titles=kwargs.other_titles)
      db.add(db_map)
      db.commit()
      db.refresh(db_map)
      return db_map
   except IntegrityError as e:
      db.rollback()
      print(f'IntegrityError occured: {e.orig}')