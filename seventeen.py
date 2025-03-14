from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


app = FastAPI()


@app.post("/files")
# async def create_file(file: bytes = File(...)):
# async def create_file(file: bytes | None = File(None, description=" file read as bytes")):
async def create_file(files: list[bytes] = File(..., description=" file read as bytes")):
    # if not file:
    #     return {"message":"No file sent"}
    return {"file_sizes": [len(file) for file in files]}



@app.post("/uploadfiles/")
async def create_upload_file(files: list[UploadFile] = File(..., description="A file read as UploadFile")):
    return {"filename": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
    <form action="/files/" enctype="multipart/form-data" method="post">
        <input type="file" name="files" id="" multiple>
        <input type="submit">
    </form>
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
        <input type="file" name="files" id="" multiple>
        <input type="submit">
    </form>
</body>
    """
    return HTMLResponse(content=content)