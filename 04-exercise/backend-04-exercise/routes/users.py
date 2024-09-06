from fastapi import APIRouter

users = APIRouter(prefix="/users", tags=["authentication", "users"])

@users.get("/")
def welcomeUsers():
    return { "message": "Welcome to users router" }

@users.get("/users")
def get_users():
    return { "message": "Here you will get it all users that you have in database"}
