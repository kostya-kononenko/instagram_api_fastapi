from pydantic import BaseModel
from datetime import datetime

from comments.schemas import Comment
from users.schemas import User
from typing import List


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int


class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    comments: List[Comment]

    class Config:
        from_attributes = True
