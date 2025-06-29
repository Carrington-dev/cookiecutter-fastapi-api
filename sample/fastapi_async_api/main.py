from fastapi import FastAPI
from app.api.v1 import auth

app = FastAPI(title="FastAPI Async API")


app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
async def home():
    return {"message": "Welcome to FastAPI Async API"}
