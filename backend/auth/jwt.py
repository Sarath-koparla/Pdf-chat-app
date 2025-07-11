# backend/auth/jwt.py
from jose import JWTError, jwt
from datetime import datetime, timedelta

# Secret key to sign the JWT
SECRET_KEY = "your-secret-key"  # use a strong random value in real apps
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})  # ⏳ Add expiry
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
