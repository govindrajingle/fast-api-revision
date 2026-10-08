from fastapi import FastAPI

app = FastAPI()


# static routes (string)
@app.get("/users/general/{user_id}")
def get_users(user_id):
    return {"user_id": user_id}


# dynamic routes
@app.get("/users/dynamic/{user_id}")
def get_users_int(user_id: int):
    return {"user_id": user_id}


# query params
# /prices?price=400
# handle optional parameter as well if no price is given
@app.get("/prices")
def get_prices(price: int = None):
    return {"price": price}
