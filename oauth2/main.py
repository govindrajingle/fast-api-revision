from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import FastAPI, HTTPException, Depends, Header
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext

app = FastAPI()

# jwt config
SECRET_KEY = "MY_SECRET_FOR_ENC"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRY_MINUTES = 30

# password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth setup
oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

# dummy fake db
fake_user_db = {
    "admin": {
        "username": "admin",
        "hashed_password": "$2b$12$MlAhhZvHfbiospGqy7tBL.z32OWidEe8A22ahdRGziwSicMIttpRu",
    }
}


# hash password
def hash_password(password: str):
    return pwd_context.hash(password)


# verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# create token
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


# log in api token generate with oauth2 form
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="invalid credentials")
    access_token = create_token({"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}


# verify token
def verify_token(token: str = Depends(oauth2_schema)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="invalid token")
        return username
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="invalid or expired token")


# protected route
@app.get("/secure")
def secure_data(user: str = Depends(verify_token)):
    return {"message": "secure data accessed", "username": user}
