from pydantic_settings import BaseSettings
from .paths import AppPaths

class Settings(BaseSettings):
    youtube_api_key: str
    # database_url: str

    class Config:
      env_file = str(AppPaths().core_dir / ".env") # Path to .env (string)

# Singleton Instance
settings = Settings()

# Test
if __name__ == "__main__":
  print(settings.youtube_api_key)
