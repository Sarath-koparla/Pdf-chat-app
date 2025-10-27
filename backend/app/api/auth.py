from fastapi import APIRouter
from app.schemas.user_schema import UserCreate
from app.services.auth_service import create_user

router = APIRouter()

@router.post("/signup")
async def signup(user: UserCreate):
    result = await create_user(user)
    return result
from app.schemas.user_schema import UserLogin
from app.services.auth_service import login_user

@router.post("/login")
async def login(user: UserLogin):
    return await login_user(user)

from fastapi import Depends
from app.utils.dependencies import get_current_user

@router.get("/me")
async def get_me(current_user: dict = Depends(get_current_user)):
    return {
        "message": "You are authenticated!",
        "user": current_user
    }
