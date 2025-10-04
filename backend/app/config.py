import os
from pydantic import BaseModel


class Settings(BaseModel):
    database_url: str = os.getenv("DATABASE_URL", os.getenv("POSTGRES_URI", "postgresql+psycopg2://postgres:postgres@localhost:5432/aitube"))
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    env: str = os.getenv("ENV", "development")
    secret_key: str = os.getenv("SECRET_KEY", "changeme")
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    youtube_api_key: str | None = os.getenv("YOUTUBE_API_KEY")


settings = Settings()


