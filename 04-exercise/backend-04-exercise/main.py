from fastapi import FastAPI
from routes.users import users
from routes.notes import notes


app = FastAPI()

app.include_router(users)
app.include_router(notes)

@app.get('/')
async def root():
    return {"message": "Welcome to 04-example-backend"}
