from fastapi import APIRouter, Depends
from app.auth.routes import get_current_user
from app.models import Users
from app.schema import UserResponse


router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me")
def me(current_user: Users = Depends(get_current_user), response_model=UserResponse):
    return UserResponse(**current_user.__dict__)