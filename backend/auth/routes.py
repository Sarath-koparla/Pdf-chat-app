from fastapi import APIRouter ,HTTPException
from schemas.user import Userlogin
from auth.jwt import create_access_token

router =APIRouter()

@router.post("/login")
def login(user :Userlogin):
    if user.email !="sarath.koparla@gmail.com" or user.password != "123456":
        raise HTTPException(status_code=401,detail="invalid email")
   
    token_data = {"sub": user.email}  # 'sub' = subject = user
    token = create_access_token(token_data)

    return {
        "access_token": token,
        "token_type": "bearer"
    }
