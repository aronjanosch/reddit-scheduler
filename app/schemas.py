from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class RedditPostBase(BaseModel):
    link: str
    comment: str
    schedule_time: datetime
    subreddit: str

class RedditPostCreate(RedditPostBase):
    pass

class RedditPostUpdate(RedditPostBase):
    pass

class RedditPostDB(RedditPostCreate):
    id: Optional[str] = None
    created: datetime = Field(default_factory=datetime.now, description="The time the post was created")
    modified: datetime = Field(default_factory=datetime.now, description="The time the post was last modified")

class UserBase(BaseModel):
    full_name: Optional[str] = Field(None, description="The user's full name")
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    email: str

class UserDB(UserBase):
    id: Optional[str] = None  # MongoDB ID
    created: datetime = Field(default_factory=datetime.now)
    modified: datetime = Field(default_factory=datetime.now)
    email: str = Field(..., description="The user's email address")