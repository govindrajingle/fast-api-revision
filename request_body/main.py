from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str = "Default User"
    age: int = 18


@app.post("/create-user")
def create_user(user: User):
    return user
