from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Base

from config.database import engine
from routes.users import users
from routes.notes import notes
from routes.auth import auth
        
app = FastAPI()

origins = [
    "http://localhost:8000",
    "https://localhost:8000",
    "http://localhost:5173",
    "https://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

try:
    Base.metadata.create_all(bind=engine)
except Exception as error:
    print('Error connecting with database')
    exit()

app.include_router(auth)
app.include_router(users)
app.include_router(notes)

@app.get('/')
async def root():
    return {"message": "Welcome to 04-example-backend"}
