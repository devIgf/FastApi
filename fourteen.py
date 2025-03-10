from typing import Literal, Union
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


@app.get("/")
async def root():
    return "Hello World"


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name:str |None = None



class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hashed(raw_password: str):
    return f"supersecret{raw_password}"


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hashed(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("user_in.dict", user_in.dict())
    print("User 'Saved'.")
    return user_in_db


@app.post("/user/",response_model=UserOut)
async def create_user(user_in:UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type:str = "Car"


class PlaneItem(BaseItem):
    type:str = "plane"
    size:int


items = {
    "item1":{"description":"All my freinds drivea lon rder","type":"car"},
    "item2":{"description":"Misuc is my aeroplane, it's my aeroplane","type":"plan","size":5}
}


@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id:Literal["item1","item2"]):
    return items[item_id]


class ListItem(BaseModel):
    name:str
    description: str


list_items = [
    {"name":"foo", "description":"There comes my hero"},
    {"name":"Red", "description":"Itis my aeroplane"}
]


@app.get("/list_items/")
async def read_items():
    return items


@app.get("/arbitrary", response_model=dict[str, float])
async def get_arbitrary():
    return {"foo":1, "bar":"2"}