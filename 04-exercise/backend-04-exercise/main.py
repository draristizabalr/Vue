from fastapi import FastAPI
from routes.users import users

app = FastAPI()

app.include_router(users)

@app.get('/')
async def root():
    return {"message": "¡Hola FastAPI!"}

@app.get('/url')
async def getURL():
    return { "url": "https://mouredev.com/python" }