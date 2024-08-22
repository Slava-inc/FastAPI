from sqlalchemy.orm import Session
from .models import Map_Object, Images
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


def AddImage(db: Session, **kwargs):

   try:
      id = db.query(func.max(Images.id)).scalar()
      if id == None:
         id = 1
      else:
         id += 1

      db_image = Images(id=id, name=kwargs['name'],
                           file=kwargs['file'])

      db.add(db_image)
      db.commit()
      db.refresh(db_image)
      return db_image
   except IntegrityError as e:
      db.rollback()
      print(f'IntegrityError occured: {e.orig}')