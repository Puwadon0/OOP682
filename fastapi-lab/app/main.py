from fastapi import FastAPI, Depends, HTTPException
from typing import List
from .models import Task, TaskCreate
from .services import TaskService
from .repositories import SqlTaskRepository
from .database import SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_task_service(db: Session = Depends(get_db)):
    repo = SqlTaskRepository(db)
    return TaskService(repo)

@app.get("/tasks", response_model=List[Task])
def read_tasks(service: TaskService = Depends(get_task_service)):
    return service.get_tasks()

@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate, service: TaskService = Depends(get_task_service)):
    return service.create_task(task)

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskCreate, service: TaskService = Depends(get_task_service)):
    return service.update_task(task_id, task)

@app.put("/tasks/{task_id}/complete")
def mark_as_complete(task_id: int, service: TaskService = Depends(get_task_service)):
    updated_task = service.complete_task(task_id)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task marked as complete", "task": updated_task}