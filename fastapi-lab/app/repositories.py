from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session
from .models import Task, TaskCreate
from . import models_orm 

class ITaskRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Task]: pass

    @abstractmethod
    def create(self, task: TaskCreate) -> Task: pass
        
    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]: pass
    
    @abstractmethod
    def update(self, task_id: int, task: TaskCreate) -> Optional[Task]: pass

    @abstractmethod
    def get_by_title(self, title: str) -> Optional[Task]: pass

class SqlTaskRepository(ITaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Task]:
        return self.db.query(models_orm.TaskORM).all()
    
    def get_by_title(self, title: str) -> Optional[Task]:
        return self.db.query(models_orm.TaskORM).filter(models_orm.TaskORM.title == title).first()
    
    def create(self, task_in: TaskCreate) -> Task:
        db_task = models_orm.TaskORM(**task_in.dict())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task
    
    def get_by_id(self, task_id: int) -> Optional[Task]:
        return self.db.query(models_orm.TaskORM).filter(models_orm.TaskORM.id == task_id).first()

    def update(self, task_id: int, task_in: TaskCreate) -> Optional[Task]:
        db_task = self.get_by_id(task_id)
        if db_task:
            for key, value in task_in.dict().items():
                setattr(db_task, key, value)
            self.db.commit()
            self.db.refresh(db_task)
        return db_task


class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self.tasks = []
        self.current_id = 1

    def get_all(self) -> List[Task]:
        return self.tasks

    def get_by_title(self, title: str) -> Optional[Task]:
        for t in self.tasks:
            if t.title == title: return t
        return None
    
    def create(self, task_in: TaskCreate) -> Task:
        task = Task(id=self.current_id, **task_in.dict())
        self.tasks.append(task)
        self.current_id += 1
        return task

    def get_by_id(self, task_id: int) -> Optional[Task]:
        for t in self.tasks:
            if t.id == task_id: return t
        return None
    
    def update(self, task_id: int, updated_task: TaskCreate) -> Optional[Task]:
        for t in self.tasks:
            if t.id == task_id:
                for key, value in updated_task.dict().items():
                    setattr(t, key, value)
                return t
        return None