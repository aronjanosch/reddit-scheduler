from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# Create a model for a reddit post like the one in schemas.py
# Use the pydantic Field class to add a description to the fields
# Use the datetime class to add a default value to the schedule_time field and use datetime to set the fields created and modified
# Use the typing module to add an optional id field to the model
class RedditPost(BaseModel):
    link: str = Field(..., description="The link to the Reddit post")
    comment: str = Field(..., description="The comment to be posted with the Reddit link")
    schedule_time: datetime = Field(default_factory=datetime.now, description="The time the post will be scheduled to be posted")
    created: datetime = Field(default_factory=datetime.now, description="The time the post was created")
    modified: datetime = Field(default_factory=datetime.now, description="The time the post was last modified")