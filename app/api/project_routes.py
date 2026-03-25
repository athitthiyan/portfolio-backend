from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.project_service import get_all_projects
from app.schemas.project_schema import ProjectResponse

router = APIRouter()


@router.get("/projects", response_model=list[ProjectResponse])
def fetch_projects(db: Session = Depends(get_db)):
    return get_all_projects(db)
