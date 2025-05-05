from googleapiclient.discovery import build
from application.core.config import settings

# Initialize the YouTube Data API client
youtube = build('youtube', 'v3', developerKey=settings.youtube_api_key)

if __name__ == "__main__":
  print(settings.youtube_api_key)

