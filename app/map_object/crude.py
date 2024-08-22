from sqlalchemy.orm import Session
from .models import Map_Object
from .schemas import MapCreate
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from datetime import datetime

def AddData(db: Session, **kwargs):

   try:
      id = db.query(func.max(Map_Object.id)).scalar()
      if id == None:
         id = 1
      else:
         id += 1
      date = datetime.strptime(kwargs['add_time'], '%Y-%m-%d %H:%M:%S')
      db_map = Map_Object(id=id, add_time=date, user_id=kwargs['user'],
                            raw_data=kwargs['raw_data'], images=kwargs['images'], status='new')

      db.add(db_map)
      db.commit()
      db.refresh(db_map)
      return db_map
   except IntegrityError as e:
      db.rollback()
      print(f'IntegrityError occured: {e.orig}')