from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.dialects.postgresql import ARRAY
from app.db.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    tech_stack = Column(ARRAY(String), nullable=True)
    demo_link = Column(String, nullable=True)
    github_link = Column(String, nullable=True)
    display_date = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
