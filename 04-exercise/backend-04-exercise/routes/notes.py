from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status, Cookie
from sqlalchemy.orm import Session

from config.database import get_db
from schemas.notes import Note, NoteCreate
from functions.notes import get_notes, get_note_by_user_id, get_note_by_user_id_and_title, create_note, delete_note
from functions.auth import get_current_user, verify_user

notes = APIRouter(
    prefix="/notes",
    tags=["notes"],
    dependencies=[Depends(verify_user)]
)

@notes.get("/all_notes")
def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_notes(db=db, skip=skip, limit=limit)

@notes.get("/")
async def read_notes_by_user(token: Annotated[str, Cookie()], skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    
    user = await get_current_user(token=token, db=db)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not authorized")
    
    return get_note_by_user_id(db=db, user_id=user.id, skip=skip, limit=limit) #type: ignore

@notes.post("/")
async def create_note_db(token: Annotated[str, Cookie()], note: NoteCreate, db: Session = Depends(get_db)):
    
    user = await get_current_user(token=token, db=db)
    
    find_note = get_note_by_user_id_and_title(db=db, title=note.title, user_id=user.id) #type: ignore
    
    if find_note:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title note already exist")
    
    return create_note(db=db, note=note, user_id=user.id) #type: ignore
