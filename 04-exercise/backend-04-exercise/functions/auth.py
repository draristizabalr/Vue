from fastapi import Depends, HTTPException, status, Cookie
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta, datetime, timezone
from typing import Annotated
from sqlalchemy.orm import Session
from functions.users import pwd_context, get_user_by_username
from config.database import get_db
import jwt
from jwt.exceptions import InvalidTokenError
from os import getenv
from dotenv import load_dotenv

from schemas.users import TokenData, User

load_dotenv()

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str, db: Session):
    user = get_user_by_username(db=db, username=username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El nombre de usuario o la contraseña son incorrectas",
            headers={ "WWW-Authenticate": "Bearer" }
        )
    if not verify_password(plain_password=password, hashed_password=user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El nombre de usuario o la contraseña son incorrectas",
            headers={ "WWW-Authenticate": "Bearer" }
        )

    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    
    to_encode.update({ "exp": expire })
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt    

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    credential_exceptions = HTTPException( 
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="You are not authorized",
        headers={ "WWW-Authenticate": "Bearer" }
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) # type: ignore
        username: str = payload.get("sub")
        if username is None:
            raise credential_exceptions
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credential_exceptions
    
    user = get_user_by_username(username=token_data.username, db=db)
    
    if not user:
        raise credential_exceptions
    
    return user
