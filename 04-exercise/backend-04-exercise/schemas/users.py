from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    
class UserCreate(UserBase):
    password: str
    
class User(BaseModel):
    id: int
    name: str
    email: str
    hash_password: str
    