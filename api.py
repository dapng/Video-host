import shutil
import filetype
from typing import List
from starlette.responses import StreamingResponse
from starlette.templating import Jinja2Templates
from fastapi import FastAPI, Form, UploadFile, File, APIRouter, BackgroundTasks, HTTPException


from schemas import UploadVideo, GetVideo, Message
from models import Video, User
from services import write_video

video_router = APIRouter()


@video_router.post("/")
async def create_video(
        background_tasks: BackgroundTasks,
        title: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(...)
):
    file_name = f'media/{file.filename}'
    if file.content_type == 'video/mp4':
        background_tasks.add_task(write_video, file_name, file)
    else:
        raise HTTPException(status_code=418, detail="Это не mp4")
    info = UploadVideo(title=title, description=description)
    user = await User.objects.first()
    return await Video.objects.create(file=file_name, user=user, **info.dict())


@video_router.get("/video/{video_pk}", responses={404: {"model": Message}})
async def get_video(video_pk: int):
    file = await Video.objects.select_related('user').get(pk=video_pk)
    file_like = open(file.dict().get('file'), mode="rb")
    return StreamingResponse(file_like, media_type="video/mp4")

