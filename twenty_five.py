# Dependencies in path operation decorators

from fastapi import Body, Depends, FastAPI, HTTPException, Header


app = FastAPI()


async def verify_token(x_token: str = Header(...)):
    if x_token != "Fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-token header invalid")
   

async def verify_key(x_key: str = Header(...)):
    if x_key != "Fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-token header invalid")
    return x_key



# app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get("/items", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items(blah: str = Depends(verify_token)):
    print(blah)
    return [{"item" : "Foo"}, {"item" : "Bar"}]


@app.get("/users/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_users():
    return [{"username":"Don Corloeon"}, {"username":"Monace"}]