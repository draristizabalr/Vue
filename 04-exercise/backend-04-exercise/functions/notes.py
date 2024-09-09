from sqlalchemy.orm import Session

from models.notes import Note
from schemas.notes import NoteBase, NoteCreate

def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Note).offset(skip).limit(limit).all()

def get_note_by_user_id(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(Note).filter(Note.user_id == user_id).offset(skip).limit(limit).all()

def get_note_by_user_id_and_title(db: Session, title: str, user_id: int):
    return db.query(Note).filter(Note.title == title, Note.user_id == user_id).first()

def create_note(db: Session, note: NoteCreate):
    db_note = Note(**note.model_dump())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def delete_note(db: Session, title: str, user_id: int):
    note = get_note_by_user_id_and_title(db=db, title=title, user_id=user_id)
    if not note:
        return
    
    db.delete(note)
    db.commit()
    
    return note
