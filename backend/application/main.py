from fastapi import FastAPI
from application.routes.youtube_controller import router as youtube_router

app = FastAPI()

app.include_router(youtube_router)