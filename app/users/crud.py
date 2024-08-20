from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate, UserUpdate
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func


pwd_context = CryptContext(schemes=['bcrypt'])

def get_users(db: Session):
   return db.query(User).all()

def get_user(db: Session, user_id:int):
   return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
   hashed_password = pwd_context.hash(user.password)
   try:
      id = db.query(func.max(User.id)).scalar()
      if id == None:
         id = 1
      else:
         id += 1
      db_user = User(username=user.username, email=user.email, hashed_password= hashed_password, id=id)
      db.add(db_user)
      db.commit()
      db.refresh(db_user)
      return db_user
   except IntegrityError as e:
      db.rollback()
      print(f'IntegrityError occured: {e.orig}')

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
      db.delete(db_user)
      db.commit()

    return db_user
