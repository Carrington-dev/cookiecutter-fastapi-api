from fastapi import FastAPI
from app.api.v1 import auth

app = FastAPI(title="{{ cookiecutter.project_name }}")


app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
async def home():
    return {"message": "Welcome to {{ cookiecutter.project_name }}"}
