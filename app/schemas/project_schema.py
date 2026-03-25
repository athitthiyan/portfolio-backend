from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str
    tech_stack: Optional[List[str]] = None
    demo_link: Optional[str] = None
    github_link: Optional[str] = None
    display_date: Optional[str] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
