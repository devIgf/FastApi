from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel,HttpUrl

app = FastAPI()


class Image(BaseModel):
    url : HttpUrl
    name : str


class Items(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None
    # une list accepte les doublons 
    # tags : list[str] = set()

    # une list N'accepte pas les doublons
    tags : set[str] = set()
    image : list[Image] | None = None


class Offer(BaseModel):
    name : str
    description : str | None = None
    price : float
    items : list[Items]


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Items):
    results = {"item_id":item_id, "item":item}
    return results


@app.post("/offers")
async def create_offer(offer:Offer = Body(...,embed=True)):
    return offer


@app.post("/images/multiple")
async def create_multiple_images(images: list[Image]):
    return images


@app.post("/blash")
async def create_same_blashs(blashs:dict[int, float]):
    return blashs