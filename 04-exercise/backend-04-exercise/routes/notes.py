from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models import Base
from schemas.notes import Note, NoteCreate

from functions.notes import get_notes, get_note_by_user_id, get_note_by_user_id_and_title, create_note

notes = APIRouter(prefix="/notes", tags=["notes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@notes.get("/", response_model=list[Note])
def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_notes(db=db, skip=skip, limit=limit)

@notes.get("/user_notes", response_model=list[Note])
def read_notes_by_user(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_note_by_user_id(db=db, user_id=user_id, skip=skip, limit=limit)

@notes.post("/", response_model=Note)
def create_note_db(note: NoteCreate, db: Session = Depends(get_db)):
    find_note = get_note_by_user_id_and_title(db=db, title=note.title, user_id=note.user_id)
    
    if find_note:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title note already exist")
    
    return create_note(db=db, note=note)


