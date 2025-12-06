from pydantic import AnyUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "My App (Dev)"

    DATABASE_URL: AnyUrl

    class Config:
        env_file = ".env.dev"

settings = Settings()
