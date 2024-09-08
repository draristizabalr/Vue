from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.database import SessionLocal, engine
from models.users import Base
from schemas.users import User, UserBase, UserCreate

from functions.users import get_users, get_user_by_id, get_user_by_email, create_user, delete_user

try:
    Base.metadata.create_all(bind=engine)
except Exception as error:
    print('Error connecting with database')
    exit()

users = APIRouter(prefix="/users", tags=["authentication", "users"])

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@users.get("/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users

@users.get("/user_id/{id}", response_model=User)
def read_user_by_id(id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db=db, user_id=id)
    if user:
        return user
            
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID user not found")

@users.get("/user_email/{email}", response_model=User)
def read_user_by_email(email: str, db: Session = Depends(get_db)):
    user = get_user_by_email(db=db, email=email)
    if user:
        return user
                
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email user not found")

@users.post("/", response_model=User)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    return create_user(db=db, user=user)

@users.delete("/{email}")
def delete_user_db(email: str, db: Session = Depends(get_db)):
    user = delete_user(db=db, email=email)
    if user:
        return {
            "message": "User deleted successfully",
            "user": user
        }
        
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email not registered")
