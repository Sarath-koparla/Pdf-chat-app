from fastapi import FastAPI
from typing import Optional
from auth.routes import router as auth_router
from chat.routes import router as chat_router
from schemas.openapi_schema import custom_openapi

app =FastAPI()

app.include_router(auth_router)
app.include_router(chat_router)
app.openapi=lambda:custom_openapi(app)
