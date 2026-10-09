from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []


class Todo(BaseModel):
    id: int
    title: str
    completed: bool


@app.post("/create")
def create_todo(todo: Todo = None):
    todos.append(todo)
    return {"message": "TODO added", "data": todos}


@app.get("/todos")
def get_all_todos():
    return {"data": todos}


@app.patch("/todo")
def update_todo(todo: Todo):
    for i, current in enumerate(todos):
        if current.id == todo.id:
            todos[i] = todo
            return todo
    return {"message": "TODO not found"}


@app.put("/todo")
def replace_todo(todo: Todo):
    for i, current in enumerate(todos):
        if current == todo:
            todos.remove(current)
            todos.append(todo)
            return todo
    return {"message": "TODO not found"}


@app.delete("/delete/{id}")
def delete_todo(id: int):
    for current in todos:
        if current.id == id:
            todos.remove(current)
            return todos
    return {"message": "TODO not found"}
