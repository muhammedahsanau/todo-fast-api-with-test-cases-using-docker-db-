from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List  # Import List from typing
from app.database import get_db
from app.todo.schema import TodoCreate, TodoUpdate, TodoResponse
from app.todo.service import (
    create_todo,
    get_todo_by_id,
    get_all_todos,
    update_todo,
    delete_todo,
)

router = APIRouter()

@router.post("/", response_model=TodoResponse)
def create_todo_route(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_todo(db, todo)

@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo_route(todo_id: int, db: Session = Depends(get_db)):
    todo = get_todo_by_id(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.get("/", response_model=List[TodoResponse])  # Use List here
def get_todos_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_todos(db, skip, limit)

@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo_route(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    updated_todo = update_todo(db, todo_id, todo)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo

@router.delete("/{todo_id}", response_model=TodoResponse)
def delete_todo_route(todo_id: int, db: Session = Depends(get_db)):
    deleted_todo = delete_todo(db, todo_id)
    if not deleted_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return deleted_todo
