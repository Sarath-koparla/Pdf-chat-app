from pydantic import BaseModel , EmailStr

class Userlogin(BaseModel):
    email :EmailStr
    password:str