from fastapi import Body, FastAPI, Form
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
async def home():
    return "Hello Monace!"



@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    print("password", password)
    return {"username",username}


class User(BaseModel):
    username:str
    password:str

@app.post("/login_json/")
async def login_json(user:User):
    return user


@app.post("/login_body/")
async def login_body(username: str = Body(...), password: str = Body(...)):
    print("password", password)
    return {"username", username}