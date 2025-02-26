from enum import Enum
from typing import Optional
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def base_get_route():
    return {"message":"hello world"}


@app.post("/")
async def post():
    return {"message": "hollo from the post route"}


@app.put("/")
async def put():
    return {"message":"hello from the put route"}


@app.get("/users")
async def list_users():
    return {"message":"list users route"}


@app.get("/users/{user_id}")
async def get_user(user_id):
    return {"user_id":user_id}


@app.get("/users/me")
async def get_current_user():
    return {"message":"this is the current user"}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name:FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name":food_name, "message":"you are healthy"}
    
    if food_name.value == 'fruits':
        return {"food_name":food_name, "message":"you are still healthy, but like sweet things"}
    
    return {"food_name":food_name, "message":"I like chocolat milk"}


fake_items_db = [{"item_name":"Food"},{"item_name":"Bar"},{"tiem_name":"Baz"}]


@app.get("/items")
async def list_items(skip:int=0, limit:int=10):
    return fake_items_db[skip:skip+limit]


@app.get("/items/{item_id}")
async def get_item(
    item_id: str,sample_query_param: str = Query(...), q:Optional[str]=None, short:bool=False
    ):
    item = {"item_id":item_id, "sample_query_param":sample_query_param}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {
                "description":"Lorem ipsum dolor sit ame consectetur adipiscing elit. Aenean iaculis."
             }
            )
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id:int,item_id: str, q:Optional[str]=None, short:bool=False):

    item = ({"item_id":item_id, "owner_id":user_id})
    
    if q:
        item.update({"q":q})

    if not short:
        item.update(
            {
                "description":"Lorem ipsum dolor sit ame consectetur adipiscing elit. Aenean iaculis."
             }
            )
    return item


class Item(BaseModel):
    name:str
    description: str | None = None
    price:float
    tax:float | None = None


@app.post("/items")
async def create_item(item:Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax":price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def create_with_put(item_id:int, item:Item, q:str | None = None):
    result = {"item_id":item_id, **item.dict()}
    if q:
        result.update({"q":q})

    return result


@app.get("/itemsread")
# async def read_items(q:str = Query(..., min_length=3, max_length=10)):
async def read_items(q: str | None = Query(
    None, 
    min_length=3, 
    max_length=10, 
    title="Sample title string", 
    description="Sample discription string",
    alias="item-query"    
    )):
    results = {"items":[{"item_id":"Food"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results



@app.get("/items_hidden")
async def hidden_query_route(hidden_query: str | None = Query(None, include_in_schema=False)):
    if hidden_query:
        return {"hidden_query":hidden_query}
    return {"hidden_query":"Not found"}