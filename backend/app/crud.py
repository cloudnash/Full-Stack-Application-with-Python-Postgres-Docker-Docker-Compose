# backend/app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def list_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(name=project.name, description=project.description)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def list_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).offset(skip).limit(limit).all()

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        status=task.status or "todo",
        project_id=task.project_id,
        assignee_id=task.assignee_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def list_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()

def list_tasks_with_details(db: Session, skip: int = 0, limit: int = 100):
    q = db.query(
        models.Task.id,
        models.Task.title,
        models.Task.description,
        models.Task.status,
        models.Project.name.label("project_name"),
        models.User.name.label("assignee_name")
    ).join(models.Project, models.Task.project_id == models.Project.id
    ).join(models.User, models.Task.assignee_id == models.User.id
    ).offset(skip).limit(limit)
    return q.all()
