from user.schemas import UserOut

from pydantic import BaseModel


class FollowerCreate(BaseModel):
    username: str


class FollowerList(BaseModel):
    user: UserOut
    subscriber: UserOut
