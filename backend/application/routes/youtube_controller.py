from fastapi import APIRouter, HTTPException
from application.services import youtube_service
from googleapiclient.errors import HttpError

router = APIRouter(prefix="/youtube", tags=["youtube-api"])

@router.get("/video-info/{video_id}")
async def get_video_info(video_id: str):
    try:
        return youtube_service.get_video_info_by_id(video_id)
    except HttpError as err:
        raise HTTPException(status_code=500, detail=str(err))