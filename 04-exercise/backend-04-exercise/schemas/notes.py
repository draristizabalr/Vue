from pydantic import BaseModel

class NoteBase(BaseModel):
    title: str
    description: str
    
class NoteCreate(NoteBase):
    user_id: int

class Note(NoteCreate):
    id: int
    
    class Config:
        from_attributes = True
