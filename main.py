from fastapi import FastAPI

app = FastAPI()


# Home Route
@app.get("/")
def homepage():
    return {"message": "hello, fastapi"}
