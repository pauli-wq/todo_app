from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class ToDo(Base):
    __tablename__ = "tasks"
    __table_args__ = {'schema': 'todo_app'}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    description = Column(String(255))
    completed = Column(Boolean, default=False)
