# backend/auth/dependencies.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel


SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

# This tells FastAPI where the token will come from
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# What we expect inside the token
class TokenData(BaseModel):
    email: str | None = None

# Core function: to get current user from JWT
def get_current_user(token: str = Depends(oauth2_scheme)) -> TokenData:
    try:
        # Decode the JWT token using secret and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")  # "sub" is the subject = email
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")
        return TokenData(email=email)

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
