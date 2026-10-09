from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()


class UserNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UserNotFoundException)
def user_not_found_handler(exception: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"status": "error", "message": f"user {exception.name} not found"},
    )


@app.get("/user/{name}")
def get_user(name: str):
    if name != "govind":
        raise UserNotFoundException(name)
    return {"name": name}
