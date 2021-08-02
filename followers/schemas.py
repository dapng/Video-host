import uuid
from typing import List
from user.schemas import UserOut

from pydantic import BaseModel

from user.schemas import User


class FollowerCreate(BaseModel):
    username: str


class FollowerList(BaseModel):
    user: UserOut
    subscriber: UserOut
