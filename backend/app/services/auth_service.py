from fastapi import HTTPException, status
from app.db.mongodb import db
from app.utils.security import hash_password

async def create_user(user_data):
    # Check if user already exists
    existing_user = await db["users"].find_one({"email": user_data.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    # Hash the password
    hashed_pw = hash_password(user_data.password)

    # Insert into database
    await db["users"].insert_one({
        "email": user_data.email,
        "password": hashed_pw
    })

    return {"message": "User created successfully"}

    
from app.utils.security import verify_password
from app.utils.jwt_handler import create_access_token

async def login_user(user_data):
    user = await db["users"].find_one({"email": user_data.email})
    if not user:
        return {"error": "Invalid email or password"}

    if not verify_password(user_data.password, user["password"]):
        return {"error": "Invalid email or password"}

    token = create_access_token({"sub": user["email"]})
    return {"access_token": token, "token_type": "bearer"}
