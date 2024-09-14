from datetime import datetime, timedelta, timezone
from typing import Annotated
import jwt
from os import getenv
from dotenv import load_dotenv
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from schemas.users import Token, TokenData, User
from functions.users import pwd_context, get_user_by_username
from sqlalchemy.orm import Session
from routes.users import get_db

load_dotenv()

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

auth = APIRouter(prefix="/auth", tags=["oauth", "users", "jwt"])

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
    user = get_user_by_username(db=db, username=username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={ "message": "Username or password are not correct" })
    if not verify_password(plain_password=password, hashed_password=user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={ "message": "Username or password are not correct" })
    
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

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session):
    credential_exceptions = HTTPException( 
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={ "message": "Username or password are not correct" },
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
    
    user = get_user_by_username(username=username, db=db)
    if user is None:
        raise credential_exceptions
    
    return user

@auth.get("/")
def HelloAuth():
    return { "message": "Welcome to auth router" }

@auth.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = authenticate_user(db=db, username=form_data.username, password=form_data.password)
    
    if not user:
        raise HTTPException( 
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={ "message": "Username or password are not correct"},
            headers={ "WWW-Authenticate": "Bearer" }
        )
    
    access_token_expires = timedelta(minutes=float(ACCESS_TOKEN_EXPIRE_MINUTES)) #type: ignore
    access_token = create_access_token(
        data={ "sub": user.username }, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
