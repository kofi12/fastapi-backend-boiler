from fastapi import APIRouter, Depends
from app.auth.deps import get_current_user
from app.core.security import create_token

auth_router = APIRouter(prefix='/auth')

@auth_router.post('/token')
def login() -> str:
    admin = 1
    token = create_token(admin)
    return token

@auth_router.get('/me')
def decode(user = Depends(get_current_user)):
    return user