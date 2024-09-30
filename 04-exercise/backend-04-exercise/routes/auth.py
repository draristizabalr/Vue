from datetime import timedelta
from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException, status, Form, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from config.database import get_db
from schemas.users import Token, UserCreate
from functions.auth import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from functions.users import create_user, get_user_by_email

auth = APIRouter(prefix="/auth", tags=["oauth", "users", "jwt"])

@auth.post("/login")
async def login_for_access_token(
    response: Response,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = authenticate_user(db=db, username=form_data.username, password=form_data.password)
    
    if not user:
        raise HTTPException( 
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username or password are not correct",
            headers={ "WWW-Authenticate": "Bearer" }
        )
    
    access_token_expires = timedelta(minutes=float(ACCESS_TOKEN_EXPIRE_MINUTES)) #type: ignore
    access_token = create_access_token(
        data={ "sub": user.username }, expires_delta=access_token_expires
    )
    
    response.set_cookie(key="token", value=access_token)
    
    return Token(access_token=access_token, token_type="bearer")


@auth.post("/register")
async def register_user(user: Annotated[UserCreate, Form()], db: Session = Depends(get_db)):
    user_fond = get_user_by_email(db=db, email=user.email)
    
    if user_fond:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is already registered"
        )
    try:
        user_created = create_user(db=db, user=user)
        return user_created
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Register error. Try again"
        )
