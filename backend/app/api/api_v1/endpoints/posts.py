from fastapi import APIRouter, HTTPException, Body, status, Depends
from app.dependencies import get_current_user
from app.schemas import RedditPostCreate, RedditPostDB, RedditPostUpdate
from app.crud import create_reddit_post, update_post
router = APIRouter()

@router.post("/schedule", response_model=RedditPostDB, status_code=status.HTTP_201_CREATED)
async def create_post(post: RedditPostCreate = Body(...), firebase_user: dict = Depends(get_current_user)):
    user_id = firebase_user.get("uid")
    if not user_id:
        raise HTTPException(status_code=403, detail="Could not validate Firebase user.")
    created_post = await create_reddit_post(post, user_id)
    return created_post

@router.patch("/{post_id}", response_model=RedditPostDB)
async def update_post_data(post_id: str, post_update: RedditPostUpdate = Body(...), firebase_user: dict = Depends(get_current_user)):
    updated_post = await update_post(post_id, post_update, firebase_user['uid'])
    return updated_post

@router.get("/protected")
def read_protected(current_user: dict = Depends(get_current_user)):
    return {"message": "Protected route", "user": current_user}
