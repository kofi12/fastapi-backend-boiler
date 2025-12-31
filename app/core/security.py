from jose import JWTError, jwt
from jose.constants import ALGORITHMS
from datetime import datetime, timedelta, timezone
from app.core.config import settings

class BearAuthException(Exception):
    pass

def create_token(sub: int) -> str:
    if not settings.jwt_secret_key:
        raise ValueError("No JWT_SECRET provided")
    if not sub:
        raise ValueError("now user found")
    payload = {
        "sub": str(sub),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    }
    encoded_jwt = jwt.encode(
        payload,
        key=settings.jwt_secret_key,
        algorithm=settings.jwt_algo
    )

    return encoded_jwt

def decode_token(token: str):
    try:
        payload = jwt.decode(
            token=token,
            key=settings.jwt_secret_key,
            algorithms=[settings.jwt_algo]
        )
        return payload
    except JWTError as e:
        raise BearAuthException from e

