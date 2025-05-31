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

def get_simple_video_comments_by_id(video_id: str, max_results: int = 100):
    try:
        response = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=max_results,
            textFormat="plainText"
        ).execute()
        return response
    except HttpError as err:
        raise err
    

def get_video_comments_by_id(video_id: str, max_results: int = 20):
    try:
        comment_threads = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=max_results,
            textFormat="plainText"
        ).execute()

        comments_data = []

        for thread in comment_threads.get("items", []):
            top_comment_snippet = thread["snippet"]["topLevelComment"]["snippet"]
            comment_id = thread["snippet"]["topLevelComment"]["id"]
            reply_count = thread["snippet"].get("totalReplyCount", 0)

            comment_info = {
                "id": comment_id,
                "text": top_comment_snippet["textDisplay"],
                "author": top_comment_snippet["authorDisplayName"],
                "likes": top_comment_snippet["likeCount"],
                "published_at": top_comment_snippet["publishedAt"],
                "reply_count": reply_count,
                "replies": []
            }

            # Buscar respostas se houver
            if reply_count > 0:
                replies_response = youtube.comments().list(
                    part="snippet",
                    parentId=comment_id,
                    maxResults=10
                ).execute()

                for reply in replies_response.get("items", []):
                    reply_snippet = reply["snippet"]
                    comment_info["replies"].append({
                        "text": reply_snippet["textDisplay"],
                        "author": reply_snippet["authorDisplayName"],
                        "likes": reply_snippet["likeCount"],
                        "published_at": reply_snippet["publishedAt"]
                    })

            comments_data.append(comment_info)

        return comments_data

    except HttpError as err:
        raise err
