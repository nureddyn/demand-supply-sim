import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str
    env: str = "development"

    class Config:
        env_file = f".env.{os.getenv('ENV', 'development')}"
        env_file_encoding = "utf-8"


settings = Settings()

"""
Usage:
from config import settings
DATABASE_URL = settings.database_url
"""
