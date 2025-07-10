from fastapi import APIRouter, Depends
from auth.dependencies import get_current_user, TokenData

router = APIRouter()

@router.get("/whoami")
def whoami(current_user: TokenData = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.email}"}
