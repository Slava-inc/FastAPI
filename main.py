from fastapi import FastAPI
from app.users.schemas import User
from app.users.database import SessionLocal
from app.users.crud import create_user

from app.map_object.schemas import MapCreate
from app.map_object.crude import submitData

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
async def submitData(data):
    kwargs = json.loads(data)
    map_create = MapCreate(title=kwargs['title'], other_titles=kwargs['other_titles'], 
                           connect=kwargs['connect'], add_time=kwargs['add_time'], user=kwargs['user'],
                           coords=str(kwargs['coords']), level=str(kwargs['level']), images=kwargs['images'])
    map = submitData(db=SessionLocal(), map_create=map_create)
    if map == None:
        return 'during submition error raised'
    return f'user {map.title} added!'

@app.post("/upload/")
async def create_upload_file(file: UploadFile):
    # do something with the file
    return {"filename": file.filename}