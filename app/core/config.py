import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Project"
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "secret")
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

settings = Settings()