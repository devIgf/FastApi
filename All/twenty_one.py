from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder


app = FastAPI()


fake_db = {}

class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] =[]


items = {
    "foo":{"name":"Foo", "price": 50.2},
    "bar": {"name":"Bar", "description":"The description for bar", "price":20.2},
    "baz":{"name":"Baz","description":None, "price":50.2, "tax":10.5,"tags":[]}
}


@app.get("/items/item_id", response_model=Item)
async def read_item(item_id: str):
    return items.get(item_id)


@app.put("/items/{id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded


@app.patch("/items/{item_id}", response_model=Item)
async def path_item(item_id: str, item:Item):
    stored_item_data = items.get(item_id)
    if stored_item_data is not None:
        stored_item_model = Item(**stored_item_data)
    else:
        stored_item_model = Item()
    update_data = item.dict(exclude_unset=True)
    update_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(update_item)
    return update_item