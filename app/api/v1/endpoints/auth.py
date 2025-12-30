from fastapi import APIRouter, Depends
from auth.deps import get_current_user

auth_router = APIRouter(prefix='/auth')

@auth_router.post('token')
def login() -> str:
    pass

@auth_router.get('/me')
def decode(user = Depends(get_current_user())):
    pass