from sqlalchemy.orm import Session
from app.models import todo_models
from app.schemas import schemas

def get_todo(db: Session, todo_id: int):
    return db.query(todo_models.ToDo).filter(todo_models.ToDo.id == todo_id).first()

def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(todo_models.ToDo).offset(skip).limit(limit).all()

def create_todo(db: Session, todo: schemas.ToDoCreate):
    db_todo = todo_models.ToDo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo: schemas.ToDoUpdate):
    db_todo = db.query(todo_models.ToDo).filter(todo_models.ToDo.id == todo_id).first()
    if db_todo:
        update_data = todo.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_todo, key, value)
        db.commit()
        db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(todo_models.ToDo).filter(todo_models.ToDo.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
        return True
    return False
