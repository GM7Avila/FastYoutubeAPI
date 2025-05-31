from pydantic_settings import BaseSettings
from pydantic import ValidationError

from .paths import AppPaths
class Settings(BaseSettings):
    youtube_api_key: str
    # database_url: str

    class Config:
      env_file = str(AppPaths().core_dir / ".env") # Path to .env (string)

try: 
  settings = Settings()   # Singleton Instance
except ValidationError as e:
   raise RuntimeError(
    "A variável de ambiente `YOUTUBE_API_KEY` está ausente ou inválida.\n\n"
    "Verifique se o arquivo em `application/core/.env` está criado e devidamente"
    "configurado.\n")


# Test
if __name__ == "__main__":
  print(settings.youtube_api_key)
