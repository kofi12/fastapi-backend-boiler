from sqlmodel import SQLModel
from app.models.users import User  # noqa: F401  (import so Alembic sees it)

Base = SQLModel
