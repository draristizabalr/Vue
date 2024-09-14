from pydantic import BaseModel
from schemas.notes import Note

class UserBase(BaseModel):
    name: str
    email: str
    
class UserCreate(UserBase):
    username: str
    password: str
    
class User(UserCreate):
    id: int
    notes_id: list[Note]
    
    class Config:
        from_attributes = True
        
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str | None = None
