from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.contact_schema import ContactCreate
from app.services.contact_service import create_contact

router = APIRouter()


@router.post("/contact")
def send_contact(data: ContactCreate, db: Session = Depends(get_db)):
    return create_contact(data, db)
