import pytest
from sqlalchemy.orm import Session
from .test_db import get_test_db
import random

from app.users.crud import create_user, delete_user
from app.users.schemas import UserCreate, UserInDBBase

@pytest.fixture
def test_db():
    for db in get_test_db():
        yield db 

CHARS = "abcdefghijklmnopqrstuvwxyz1234567890"

def random_email():
    email = "".join(random.choices(CHARS, k=8)) + "@.example.com"
    return email

def random_username():
    username = "".join(random.choices(CHARS, k=8))
    return username

def random_user():
    return UserCreate(username=random_username(), email=random_email(), password='Password123!')

def test_create_user(test_db: Session):
    user_data = random_user()
    user = create_user(db=test_db, user=user_data)

    assert user.username == user_data.username
    assert user.email == user_data.email

