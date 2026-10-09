from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Person(BaseModel):
    name: str
    email: str


# path query =  /101
# query parameter = /age=24


@app.post("/update/{id}")
def update_record(id: int, age: int, person: Person):
    # print("url", id, age, person)
    return "Request successfull"
