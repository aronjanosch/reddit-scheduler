from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Any, Optional


class User(BaseModel):
    created: datetime = Field(default_factory=datetime.now)
    modified: datetime = Field(default_factory=datetime.now)
    full_name: str = Field(default="")
    email: EmailStr
    is_active: bool = Field(default=False)
    is_superuser: bool = Field(default=False)