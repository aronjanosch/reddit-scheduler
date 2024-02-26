from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class RedditPostBase(BaseModel):
    link: str
    comment: str
    schedule_time: datetime

class RedditPostCreate(RedditPostBase):
    pass

class RedditPostDB(RedditPostCreate):
    id: Optional[str] = None
