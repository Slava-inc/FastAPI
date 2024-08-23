from fastapi import FastAPI
from app.users.schemas import User
from app.users.database import SessionLocal
from app.users.crud import create_user, get_user_byemail

from app.map_object.schemas import MapCreate
from app.map_object.crude import AddData, AddImage, ReadMap, PatchMap, ReadUserMaps

import json
from fastapi import File, UploadFile

import os

from dotenv import load_dotenv
import uvicorn

dotenv_path = os.path.join(os.path.dirname(__file__), 'env')

FSTR_DB_HOST = '127.0.0.1'
FSTR_DB_PORT = 8000

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    FSTR_DB_HOST = os.getenv("FSTR_DB_HOST")
    FSTR_DB_PORT = int(os.getenv("FSTR_DB_PORT"))
    FSTR_DB_LOGIN = os.getenv("FSTR_DB_LOGIN")
    FSTR_DB_PASS = os.getenv("FSTR_DB_PASS")    


# FastAPI instance creation
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/submitData/<id>/")
async def get_map(id: int):
    map = ReadMap(db=SessionLocal(), id=id)
    if map == None:
        return {"status": 400, "message": "Перевал с данным id не найден","id": id} 
    return map

@app.get("/submitData/<email>")
async def user_map(email: str):
    user = get_user_byemail(db=SessionLocal(), email=email)
    maps = ReadUserMaps(db=SessionLocal(), id=user.id)
    return [map for map in maps]



@app.patch("/submitData/<id>/")
async def patch_map(data:dict, id: int):

    map = PatchMap(data, db=SessionLocal(), id=id)

    return map


@app.post("/register/")
async def register(username: str, email: str, password: str):

    user_create = User(username=username, email=email, password=password)
    user = create_user(db=SessionLocal(), user=user_create)
    if user == None:
        return 'during registration error raised'
    return f'user {user.username} registered!'

@app.post("/submitData/")
async def submitData(data, files: list[UploadFile]):
    try:
        kwargs = json.loads(data)
    except:
        return {"status": 400, "message": "Ошибка формата аргумента запроса","id": None}
    try:
        map = AddData(db=SessionLocal(), add_time=kwargs['add_time'], user=kwargs['user'],
                                raw_data=kwargs['raw_data'], images=kwargs['images'], status='new')
    except:
        return {"status": 400, "message": "Ошибка формата аргумента запроса","id": None}
    if map == None:
        return {"status": 500, "message": "Ошибка подключения к базе данных","id": None}
    
    for im in kwargs['images']:
        try:
            file = AddImage(db=SessionLocal(), id=im['id'], file=files[im['id']-1], name=im['title'])
        except:
            {"status": 400, "message": "Ошибка формата аргумента запроса","id": None}    
        if file == None:
            return {"status": 500, "message": "Ошибка подключения к базе данных","id": None}    
    return {"status": 200, "message": None, "id": map.id }

if __name__ == "__main__":
    uvicorn.run(app, host=FSTR_DB_HOST, port=FSTR_DB_PORT)