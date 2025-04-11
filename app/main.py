from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.database import engine, Base
from app.auth import auth_router
from app.routes import router

app = FastAPI()

# origins = [
#     "http://localhost:4200",  # Angular local development
#     #"https://yourfrontend.com",  # Production frontend URL
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,  # Allows specific origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
#     allow_headers=["*"],  # Allows all headers
# )

app.include_router(auth_router)
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Welcome to the Blog API!"}
