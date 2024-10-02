from datetime import timedelta
from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException, status, Form
from sqlalchemy.orm import Session

from config.database import get_db
from schemas.users import Token, UserCreate, UserBase
from functions.auth import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from functions.users import create_user, get_user_by_email, get_user_by_username

auth = APIRouter(prefix="/auth", tags=["oauth", "users", "jwt"])

@auth.post("/login")
async def login_for_access_token(
    user: UserBase,
    db: Session = Depends(get_db)
):
    auth_user = authenticate_user(username=user.username, password=user.password, db=db)
    
    if not auth_user:
        raise HTTPException( 
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El nombre de usuario o la contraseña son incorrectas",
            headers={ "WWW-Authenticate": "Bearer" }
        )
    
    access_token_expires = timedelta(minutes=float(ACCESS_TOKEN_EXPIRE_MINUTES)) #type: ignore
    access_token = create_access_token(
        data={ "sub": user.username }, expires_delta=access_token_expires
    )
    
    return Token(access_token=access_token, token_type="bearer")


@auth.post("/register")
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    user_email = get_user_by_email(db=db, email=user.email)
    
    if user_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya se encuentra registrado"
        )
        
    user_username = get_user_by_username(db=db, username=user.username)
    
    if user_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El nombre de usuario ya se encuentra registrado"
        )
    
    try:
        user_created = create_user(db=db, user=user)
        return user_created
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Register error. Try again"
        )

