from sqlalchemy.orm import Session
from app.models.contact import Contact


def create_contact(data, db: Session):
    try:
        contact = Contact(**data.model_dump())
        db.add(contact)
        db.commit()
        db.refresh(contact)
        return {"message": "Contact saved"}
    except Exception:
        db.rollback()
        raise
