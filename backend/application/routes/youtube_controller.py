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


@router.get("/comments/{video_id}")
def fetch_video_comments(video_id: str):
    try:
        comments = youtube_service.get_video_comments_by_id(video_id)
        return {"video_id": video_id, "comments": comments}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/simple-comments/{video_id}")
def fetch_video_comments(video_id: str):
    try:
        response = youtube_service.get_simple_video_comments_by_id(video_id)
        comments = []
        for item in response.get("items", []):
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)
        return {"video_id": video_id, "comments": comments}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


