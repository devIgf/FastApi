from datetime import datetime,time,timedelta
from uuid import UUID
from fastapi import Body, FastAPI,Cookie,Header

app = FastAPI()


@app.get("/items")
async def read_items(
    cookie_id: str | None = Cookie(None),
    accept_encoding: str | None = Header(None),
    sec_ch_ua: str | None = Header(None),
    user_agent: str | None = Header(None),
    x_token: list[str] | None = Header(None),
    ):

    return {
        "cookie_id": cookie_id,
        "accept_encoding":accept_encoding,
        "sec_ch_ua":sec_ch_ua,
        "user-Agent":user_agent,
        "x_token value":x_token
        }