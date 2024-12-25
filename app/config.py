from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    PY_ENV: str  # This will determine the environment (e.g., "TEST", "DEV", "PROD", etc.)

    class Config:
        env_file = ".env"

settings = Settings()
