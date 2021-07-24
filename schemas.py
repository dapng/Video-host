from typing import List
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    name: str


class UploadVideo(BaseModel):
    title: str
    description: str
    # tags: List[str] = None


class GetVideo(BaseModel):
    user: User
    video: UploadVideo

class Message(BaseModel):
    message: str

