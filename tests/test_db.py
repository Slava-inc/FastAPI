from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.users.models import Base

DATABASE_URL = "sqlite:///./test.db.sqlite"

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# table creation
Base.metadata.create_all(bind=engine)

def get_test_db():
    try:
        db = TestSessionLocal()
        yield db
    finally:
        db.close()