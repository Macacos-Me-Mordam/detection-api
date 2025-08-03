from fastapi import FastAPI, UploadFile, File
from app.auth.keycloak import programmatic_login
from app.services.s3 import upload_image_to_s3

app = FastAPI()

@app.lifespan("startup")
async def startup_event():
    token = await programmatic_login()
    app.state.keycloak_token = token

@app.post("/upload-image/")
async def upload_image(
    file: UploadFile = File(...)
):
    content = await file.read()
    url = upload_image_to_s3(
        file_bytes=content,
        filename=file.filename,
        content_type=file.content_type
    )
    return {"url": url}