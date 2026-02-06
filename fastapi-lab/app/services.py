from fastapi import HTTPException
from .repositories import ITaskRepository
from .models import TaskCreate

class TaskService:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    def get_tasks(self):
        return self.repository.get_all()

    def create_task(self, task_data: TaskCreate):
        # Challenge 2: ตรวจสอบชื่อซ้ำ (Validation Logic)
        existing = self.repository.get_by_title(task_data.title)
        if existing:
            raise HTTPException(status_code=400, detail="Task title already exists")
        return self.repository.create(task_data)

    def update_task(self, task_id: int, task_data: TaskCreate):
        updated = self.repository.update(task_id, task_data)
        if not updated:
            raise HTTPException(status_code=404, detail="Task not found")
        return updated

    def complete_task(self, task_id: int):
        # Challenge 1: Mark as Complete
        task = self.repository.get_by_id(task_id)
        if not task:
            return None
        
        # เปลี่ยนสถานะ completed เป็น True (อ้างอิงจาก TaskORM ของคุณ)
        task.completed = True 
        return self.repository.update(task_id, task)