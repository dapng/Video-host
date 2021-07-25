import shutil
from typing import List
from fastapi import Form, UploadFile, File, APIRouter
from schemas import UploadVideo, GetVideo, Message
from models import Video, User

video_router = APIRouter()


@video_router.post("/")
async def create_video(
        title: str = Form(...), description: str = Form(...), file: UploadFile = File(...)
):
    info = UploadVideo(title=title, description=description)
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    user = await User.objects.first()
    return await Video.objects.create(file=file.filename, user=user, **info.dict())



# @video_router.post("/img", status_code=201)
# async def upload_image(files: List[UploadFile] = File(...)):
#     for img in files:
#         with open(f'{img.filename}', "wb") as buffer:
#             shutil.copyfileobj(img.file, buffer)
#
#     return {"file_name": "Nice"}
# test upload image

# @video_router.post("/Video")
# async def create_video(video: Video):
#     await video.save()
#     return video

@video_router.get("/Video/{video_pk}", response_model=GetVideo, responses={404: {"model": Message}})
async def get_video(video_pk: int):
    return await Video.objects.select_related('user').get(pk=video_pk)

# @video_router.get("/test")
# async def get_test(req: Request):
#     print(req.base_url)
#     return {}
    #host info
