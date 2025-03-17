from enum import Enum
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


class Tags(Enum):
    items = "item"
    users = "users"


@app.post("/items/", 
          response_model= Item, 
          status_code=status.HTTP_201_CREATED, 
          tags=[Tags.items],
          summary="Create an Item",
        #   description="Create an item whote all the informations: "
        #   "name; description;price; tax; and a set of "
        #   "unique tags"
        response_description="The created item"
          
)
async def create_item(item: Item):
    """
    create an item white all the informations:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: require
    - **tax** if the item doesn't have tax, you can omit this
    - **tags**: a set of unique strings for this item
    """
    return item


@app.get("/items/", tags=[Tags.items])
async def read_items():
    return ({"name":"Foo", "Price":42})


@app.get("/users", tags=[Tags.users])
async def read_users():
    return ({"username":"MonaceAkg"})


@app.get("/elements/", tags=[Tags.items], deprecated=True)
async def read_element():
    return ({"item":"Foo"})