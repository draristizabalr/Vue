from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from os import getenv

load_dotenv()

USER_POSTGRES = getenv("USER_POSTGRES")
PASSWORD_POSTGRES = getenv("PASSWORD_POSTGRES")
SERVER_POSTGRES = getenv("SERVER_POSTGRES")
DB_NAME = getenv("DB_NAME")

SQLALCHEMY_DATABASE_URL = f"postgresql://{USER_POSTGRES}:{PASSWORD_POSTGRES}@{SERVER_POSTGRES}/{DB_NAME}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, bind=engine)

Base = declarative_base()
