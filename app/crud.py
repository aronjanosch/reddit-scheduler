from app.db import get_database
from app.schemas import RedditPostCreate

async def create_reddit_post(post: RedditPostCreate) -> dict:
    db = get_database()
    post_dict = post.model_dump()
    post_dict["schedule_time"] = post_dict["schedule_time"].isoformat()
    result = await db["scheduled_posts"].insert_one(post_dict)
    post_dict["id"] = str(result.inserted_id)
    return post_dict
