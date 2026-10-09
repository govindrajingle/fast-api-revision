from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()


# key = token, value = mysecrettoken
def verify_token(token: str = Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(status_code=401, detail="unauthorised")
    return {"user": "authorised user"}


@app.get("/secure-data")
def secure_data(user=Depends(verify_token)):
    return {"message": "secured data accessed", "user": user}


def common_logic():
    return {"message": "common logic executed"}


def get_current_user():
    return {"user": "guest"}


# basically reduces code duplication


@app.get("/user")
def home(user=Depends(get_current_user)):
    return user
