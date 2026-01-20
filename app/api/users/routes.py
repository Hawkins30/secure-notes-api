from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.security import hash_password

router = APIRouter(prefix="/users", tags=["users"])

# Temporary in-memory storage
fake_users_db = {}


class UserCreate(BaseModel):
    username: str
    password: str


@router.post("/register")
def register_user(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_pw = hash_password(user.password)

    fake_users_db[user.username] = {
        "username": user.username,
        "password": hashed_pw,
    }

    return {"message": "User registered successfully"}
