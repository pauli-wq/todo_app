from pydantic import BaseModel

class ToDoCreate(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

class ToDoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

class ToDo(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool

    class Config:
        orm_mode = True
