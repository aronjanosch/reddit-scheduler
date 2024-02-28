from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, EmailStr, HttpUrl, field_validator
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    PROJECT_NAME: str = "Reddit Scheduler"


    # GENERAL SETTINGS

    MULTI_MAX: int = 20

    # COMPONENT SETTINGS
    MONGO_DATABASE: str = os.getenv("MONGO_DATABASE")
    MONGO_DATABASE_URI: str = os.getenv("MONGO_DATABASE_URI")
    MONGO_DATABASE_TEST: str = os.getenv("MONGO_DATABASE_TEST")


settings = Settings()