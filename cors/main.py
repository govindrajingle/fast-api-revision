# if browser and backend are working on different browser must have the permission from backend

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# import os
# from dotenv import load_dotenv
from cors.config import settings

app = FastAPI()

# origins = os.getenv("ORIGINS", "*").split(",")

# allow frontend urls
# origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, PUT, PATCH, DELETE
    allow_headers=["*"],
)


@app.get("/")
def homepage():
    return {"message": "cors enabled api"}
