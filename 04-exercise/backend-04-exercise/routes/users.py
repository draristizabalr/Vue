from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from config.database import get_db
from schemas.users import User, UserCreate
from functions.users import get_users, get_user_by_email, create_user, delete_user
from functions.notes import delete_user_notes
from functions.auth import verify_user

users = APIRouter(
    prefix="/users",
    tags=["authentication", "users"],
    dependencies=[Depends(verify_user)]
)

@users.get("/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users

@users.delete("/{email}")
def delete_user_db(email: str, db: Session = Depends(get_db)):
    user = get_user_by_email(db=db, email=email)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email not registered")
    
    delete_user_notes(db=db, user_id=user.id) #type: ignore    
    
    user = delete_user(db=db, email=email)
    if user:
        return {
            "message": "User deleted successfully",
            "user": user
        }