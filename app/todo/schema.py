from pydantic import BaseModel

# Base schema for shared fields
class TodoBase(BaseModel):
    title: str
    description: str = None
    is_completed: bool = False

# Schema for creating a new Todo
class TodoCreate(TodoBase):
    pass

# Schema for updating an existing Todo
class TodoUpdate(TodoBase):
    pass

# Schema for reading a Todo
class TodoResponse(TodoBase):
    id: int

    class Config:
        from_attributes = True  # Use this instead of orm_mode
