from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate, UserUpdate
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'])

def get_users(db: Session):
   return db.query(User).all()

def get_user(db: Session, user_id:int):
   return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
   hashed_password = pwd_context.hash(user.password)
   db_user = User(username=user.username, email=user.email, hashed_password= hashed_password)
   db.add(db_user)
   db.commit()
   db.refresh(db_user)
   return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
      db.delete(db_user)
      db.commit()

    return db_user
