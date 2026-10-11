from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil  # file crud operation

app = FastAPI()

# step 1: Ensure folder exists
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# step 2: static files set up
# http://127.0.0.1:8000/FILES/FILENAME
app.mount("/files", StaticFiles(directory=UPLOAD_DIR), name="files")


# step 3: upload file api
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not filename:
        raise HTTPException(status_code=400, detail="file not selected")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        return {
            "message": "file upload successfull",
            "file_name": filename,
            "file_url": f"http://127.0.0.1:8000/files/{filename}",
        }


# step 4: get file api
@app.get("/files/{filename}")
def get_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=400, detail="file not found")
    return {
        "file_url": f"http://127.0.0.1:8000/files/{filename}",
    }


@app.get("/")
def homepage():
    return {"message": "file upload code running"}
