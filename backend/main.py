
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

@app.get("/")

def test1():
    return {"Testing!!"}

@app.get("/items/{id}/search")
def test2(id: int,q:str=None):
    return {"items":id ,"query":q }


class ilist(BaseModel):
    name:str
    price:float
@app.post("/pyd/")
def itemlist(item :ilist):
    return{
        "message":"pydantic is working",
         "itemsss":item
    }

class logindata(BaseModel):
    email:str
    passw:str
           

@app.post("/login")

def loginp(logg : logindata):
    return{"message":f"logged in user is {logg.email}"}




