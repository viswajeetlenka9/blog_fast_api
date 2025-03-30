from fastapi import FastAPI
# from app.database import engine, Base
from app.auth import auth_router
from app.routes import router

app = FastAPI()
app.include_router(auth_router)
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Welcome to the Blog API!"}
