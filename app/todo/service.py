from sqlalchemy.orm import Session
from app.todo.model import Todo
from app.todo.schema import TodoCreate, TodoUpdate

# Create a new Todo
def create_todo(db: Session, todo: TodoCreate):
    new_todo = Todo(
        title=todo.title,
        description=todo.description,
        is_completed=todo.is_completed,
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

# Get a Todo by ID
def get_todo_by_id(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

# Get all Todos
def get_all_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Todo).offset(skip).limit(limit).all()

# Update a Todo
def update_todo(db: Session, todo_id: int, todo_update: TodoUpdate):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo:
        db_todo.title = todo_update.title
        db_todo.description = todo_update.description
        db_todo.is_completed = todo_update.is_completed
        db.commit()
        db.refresh(db_todo)
        return db_todo
    return None

# Delete a Todo
def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
        return db_todo
    return None
