from fastapi import FastAPI
from app.users.schemas import User
from app.users.database import SessionLocal
from app.users.crud import create_user

from app.map_object.schemas import MapCreate
from app.map_object.crude import AddData

import json
from fastapi import File, UploadFile

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

@app.post("/submitData/")
async def submitData(data, files: list[UploadFile]):
    kwargs = json.loads(data)

    map = AddData(db=SessionLocal(), add_time=kwargs['add_time'], user=kwargs['user'],
                            raw_data=kwargs['raw_data'], images=kwargs['images'], status='new')
    if map == None:
        return 'during submition error raised'
    return f'map {map.raw_data["title"]} added!'

# @app.post("/upload/")
# async def create_upload_file(file: UploadFile):
#     # do something with the file
#     return {"filename": file.filename}