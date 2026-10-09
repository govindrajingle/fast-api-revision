from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.post("/create", status_code=status.HTTP_201_CREATED)
def create_user():
    return {"message": "user created"}


@app.get("/users")
def get_users():
    return {
        "status": status.HTTP_202_ACCEPTED,
        "message": "user fetched",
        "data": {"name": "Govind"},
    }


@app.get("/user/{user_id}")
def get_user_by_id(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="user not found")
    return {"id": 1, "name": "Govind"}
