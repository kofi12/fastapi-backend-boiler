from jose import JWTError, jwt
from jose.constants import ALGORITHMS
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
import os

class BearAuthException(Exception):
    pass

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET", '')
EXPIRY = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
ALGO = ALGORITHMS.HS256

def create_token(sub: str) -> str:
    if not JWT_SECRET:
        raise ValueError("No JWT_SECRET provided")
    if not sub:
        raise ValueError("now user found")
    payload = {
        "sub": sub,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=EXPIRY)
    }
    encoded_jwt = jwt.encode(
        payload,
        key=JWT_SECRET,
        algorithm=ALGO
    )

    return encoded_jwt

def decode_token(token: str):
    try:
        payload = jwt.decode(
            token=token,
            key=JWT_SECRET,
            algorithms=[ALGO]
        )
        return payload
    except JWTError as e:
        raise BearAuthException from e

