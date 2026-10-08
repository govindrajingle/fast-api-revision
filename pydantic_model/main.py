from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    email: str


class Address(BaseModel):
    user: User
    city: str
    pincode: int


# automatic data validation


@app.post("/create-user")
def create_user(user: User = None):
    return {
        "message": "User created successfully",
        "status": status.HTTP_201_CREATED,
        "data": user,
    }


# nested models
@app.post("/create-address")
def create_address(address: Address = None):
    print(address)
    return {"message": "Address created succefully", "data": address}
