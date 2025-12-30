from models.users import User
from core.security import decode_token
from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, select
from db.session import get_session

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl='/token',
    auto_error=True
)

def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_session)
):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    # need to implement db operations ...
    try:
        payload = decode_token(token)
        user_data = payload["sub"]

        return user_data
    except:
        pass