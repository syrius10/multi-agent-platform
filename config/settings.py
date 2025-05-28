from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env", extra="ignore")

    DEBUG: bool = False
    ENV: str = "development"
    DATABASE_URL: str = "sqlite:///default.db"
    AGENT_TIMEOUT: int = 30  # ✅ Add this line (default fallback)


settings = Settings()
