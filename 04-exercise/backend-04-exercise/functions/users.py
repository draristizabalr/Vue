from sqlalchemy.orm import Session
from passlib.context import CryptContext

from models import User
from schemas.users import UserBase, UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hash_password = pwd_context.hash(user.password)
    db_user = User(name=user.name, email=user.email, password=hash_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, email: str):
    user = get_user_by_email(db=db, email=email)
    if not user:
        return
    db.delete(user)
    db.commit()
    
    return user
