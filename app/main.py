from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import Base
from app.models import todo_models
from app.schemas import schemas
from app import crud
from .database import engine, get_db

todo_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/todos/", response_model=schemas.ToDo)
def create_todo(todo: schemas.ToDoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)

@app.get("/todos/", response_model=list[schemas.ToDo])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip=skip, limit=limit)
    return todos

@app.get("/todos/{todo_id}", response_model=schemas.ToDo)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_todo

@app.put("/todos/{todo_id}", response_model=schemas.ToDo)
def update_todo(todo_id: int, todo: schemas.ToDoUpdate, db: Session = Depends(get_db)):
    db_todo = crud.update_todo(db, todo_id=todo_id, todo=todo)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    success = crud.delete_todo(db, todo_id=todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"message": "Tarea eliminada satisfactoriamente"}
