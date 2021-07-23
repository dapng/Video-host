from typing import List
from pydantic import BaseModel


class UploadVideo(BaseModel):
    title: str
    description: str
    # tags: List[str] = None
