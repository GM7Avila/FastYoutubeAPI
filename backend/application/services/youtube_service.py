from application.api.youtube_api import youtube
from googleapiclient.errors import HttpError

def get_video_info_by_id(video_id: str):
    try:
        response = youtube.videos().list(
            part="snippet",
            id=video_id
        ).execute()
        return response
    except HttpError as err:
        raise err
