from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env.dev",
        extra="forbid",
    )

    PROJECT_NAME: str = "My App (Dev)"
    DATABASE_URL: AnyUrl

    # JWT / Auth
    jwt_secret_key: str = Field(validation_alias="JWT_SECRET_KEY")
    jwt_algo: str = Field(default="HS256", validation_alias="JWT_ALGO")
    access_token_expire_minutes: int = Field(
        default=60,
        validation_alias="ACCESS_TOKEN_EXPIRE_MINUTES",
    )


settings = Settings()

