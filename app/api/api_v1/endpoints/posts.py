from fastapi import APIRouter, HTTPException, Body, status
from app.schemas import RedditPostCreate, RedditPostDB
from app.crud import create_reddit_post

router = APIRouter()

@router.post("/schedule", response_model=RedditPostDB, status_code=status.HTTP_201_CREATED)
async def schedule_reddit_post(post: RedditPostCreate = Body(...)):
    scheduled_post = await create_reddit_post(post)
    if scheduled_post:
        return scheduled_post
    raise HTTPException(status_code=400, detail="Failed to schedule post")
