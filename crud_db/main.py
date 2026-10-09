from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends, HTTPException

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


@app.post("/todos")
def create_todos(title: str, db: Session = Depends(get_db_connection)):
    todo = Todo(title=title, completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {"message": "todo created", "data": todo}


@app.get("/todos")
def get_todos(db: Session = Depends(get_db_connection)):
    todos = db.query(Todo).all()
    return {"total": len(todos), "data": todos}


@app.get("/todos/{todo_id}")
def get_todo_by_id(todo_id: int, db: Session = Depends(get_db_connection)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="todo not found")
    return {"data": todo}
