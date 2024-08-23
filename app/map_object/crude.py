from sqlalchemy.orm import Session
from .models import Map_Object, Images, StatusEnum
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func, select
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


def ReadMap(db: Session, id:int):
      try:
         sel_map = select(Map_Object).where(Map_Object.id==id)
         return db.scalar(sel_map)
      except:
         print(f'map with index {id} not found')
         return None
      
def PatchMap(data:dict, db:Session, id:int):
   rows = db.query(Map_Object).filter(Map_Object.id == id)
   map = rows.first()
   
   if map == None:
      return {'state': 0, 'message': f'map with index {id} not found'}
   if not(map.status.name == 'new'):
      return {'state': 0, 'message': f'status {map.status.name} is fobidden for update'}
   if not(map.user_id == data['user']):
      return {'state': 0, 'message': f'field user is fobidden for update'}

   try:
      new_data = {'add_time':datetime.strptime(data['add_time'], '%Y-%m-%d %H:%M:%S'), 'images':data['images'], 'raw_data':data['raw_data']}
      
      rows.update(new_data)
      db.commit()
   except:
      return {'state': 0, 'message': 'update data error'}
   return {'state': 1}