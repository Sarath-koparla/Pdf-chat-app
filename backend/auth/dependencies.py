# backend/auth/dependencies.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

class TokenData(BaseModel):
    email: str | None = None

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # ✅ Step 1: Decode the JWT securely
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # ✅ Step 2: Extract subject (`sub`) from token payload
        email: str = payload.get("sub")

        if email is None:
            raise credentials_exception

        # ✅ Step 3: Return current user details
        return {"email": email}

    except JWTError:
        # ⚠️ Invalid signature, malformed token, or expired → reject
        raise credentials_exception
