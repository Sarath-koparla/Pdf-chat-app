from fastapi import APIRouter, Depends, HTTPException, status
from app.utils.dependencies import get_current_user
from app.db.mongodb import db

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/profile")
async def get_profile(current_user: dict = Depends(get_current_user)):
    email = current_user.get("sub")  # extracted from JWT

    user = await db["users"].find_one({"email": email}, {"_id": 0, "password": 0})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return {
        "message": "User profile fetched successfully",
        "user": user
    }
