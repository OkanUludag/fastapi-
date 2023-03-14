from db import DB
from typing import List

from fastapi import FastAPI

from pydantic import BaseModel



class Todo(BaseModel):
    id: int = None
    user: str
    task: str

app = FastAPI()
db = DB("todo.db")

app.curr_id = 1

app.todos: List[Todo] = []

@app.get("/")
def root():
    return "hello"

@app.get("/todos")
def get_todos():
    get_todo_query = """
    SELECT * FROM todos
    """
    data = db.call_db(get_todo_query)
    todos = []
    for element in data:
        id, user, task = element
        pass
    return app.todos

@app.get("/todo/{id}")
def get_todo(id: int):
    return "returns one task" + str(id)

@app.post("/add_todo")
def add_todo(todo: Todo):
    insert_query = """
    INSERT INTO todo (user, task)
    VALUES ( ?, ? )
    """
    # print(todo)
    # todo.id = app.curr_id
    # app.todos.append(todo)
    # app.curr_id+=1
    db.call_db(insert_query, todo.user, todo.task)
    return "Adding task"

def new_func():
    db.call_db

@app.delete("/delete_todo/{id}")
def delete_todo(id: int):
    delete_query = """
    DELETE FROM todo WHERE id = ?
    """
    db.call_db(delete_query, id)
    # app.todos = list(filter(lambda todo: todo.id != id, app.todos))
    return True

@app.put("/update_todo/{id}")
def update_todo(id: int, new_todo: Todo):
    update_todo_query = """
    UPDATE todo 
    SET user = ?, task = ?
    WHERE id = ?
    """
    db.call_db(update_todo_query, id, new_todo.user, new_todo.task)
    # for todo in app.todos:
    #    if todo.id == id:
    #       todo.user = new_todo.user
    #       todo.task = new_todo.task
    return True
