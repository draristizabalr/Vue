from pydantic import BaseModel
from schemas.notes import Note

class UserBase(BaseModel):
    name: str
    email: str
    
class UserCreate(UserBase):
    password: str
    
class User(UserBase):
    id: int
    name: str
    email: str
    password: str
    notes_id: list[Note]
    
    class Config:
        from_attributes = True
