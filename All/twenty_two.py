from fastapi import Depends, FastAPI


app = FastAPI()



async def hello():
    return "world"


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100, blah = Depends(hello)):
    return {"q":q, "skip":skip, "limit":limit, "hello":blah}

@app.get("/items/")
async def read_item(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons