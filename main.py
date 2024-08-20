from fastapi import FastAPI
from app.users.schemas import User
from app.users.database import SessionLocal
from app.users.crud import create_user


# FastAPI instance creation
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.post("/register/")
async def register(username: str, email: str, password: str):

    user_create = User(username=username, email=email, password=password)
    user = create_user(db=SessionLocal(), user=user_create)
    if user == None:
        return 'during registration error raised'
    return f'user {user.username} registered!'
