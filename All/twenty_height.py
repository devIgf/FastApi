from fastapi import FastAPI,Request
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI()

class MyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        print(f"URL: {request.url} - Temps de traitement: {process_time:.2f}s")
        return response
    
origins = [
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(MyMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI avec Middleware!"}
