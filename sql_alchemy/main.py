from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

# to connect to database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# made db operational
session_local = sessionmaker(bind=engine)

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)


# create table
Base.metadata.create_all(bind=engine)


# check db connection is alive for every request
def get_db_connection():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home(db: Session = Depends(get_db_connection)):
    return {"message": "database connection successfull"}
