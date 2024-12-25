from fastapi import FastAPI
from app.todo.router import router as todo_router
from app.database import Base, engine

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the Todo router
app.include_router(todo_router, prefix="/todos", tags=["Todos"])
