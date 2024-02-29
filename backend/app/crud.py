from fastapi import HTTPException
from app.db import get_database
from app.schemas import RedditPostCreate, RedditPostDB, UserUpdate, UserDB, UserBase

async def create_reddit_post(post: RedditPostCreate, user_id: str) -> RedditPostDB:
    db = get_database()
    collection = db["reddit_posts"]
    post_dict = post.model_dump()
    post_dict["user_id"] = user_id
    new_post = await collection.insert_one(post_dict)
    created_post = await collection.find_one({"_id": new_post.inserted_id})
    created_post["id"] = str(created_post["_id"])
    return RedditPostDB(**created_post)

async def update_post(post_id: str, post_update: dict, user_id: str) -> dict:
    db = get_database()
    posts_collection = db["scheduled_posts"]
    # Ensure the post belongs to the user trying to update it
    result = await posts_collection.update_one({"_id": post_id, "user_id": user_id}, {"$set": post_update})
    if result.modified_count:
        return await posts_collection.find_one({"_id": post_id})
    else:
        raise HTTPException(status_code=404, detail="Post not found or you do not have permission to update this post")

async def delete_post(post_id: str, user_id: str) -> bool:
    db = get_database()
    posts_collection = db["scheduled_posts"]
    # Ensure the post belongs to the user trying to delete it
    result = await posts_collection.delete_one({"_id": post_id, "user_id": user_id})
    return result.deleted_count > 0

async def get_user_by_firebase_uid(firebase_uid: str) -> UserDB:
    db = get_database()
    collection = db["users"]
    user = await collection.find_one({"firebase_uid": firebase_uid})
    if user:
        user["id"] = str(user["_id"])
        return UserDB(**user)
    else:
        return None

async def create_user(user_data: dict) -> UserDB:
    db = get_database()
    collection = db["users"]
    result = await collection.insert_one(user_data)
    user_data["id"] = str(result.inserted_id)
    print(user_data)
    return UserDB(**user_data)

async def update_user(user_update: dict, user_id: str) -> dict:
    db = get_database()
    users_collection = db["users"]
    # Update user document; you might need to convert user_update from Pydantic model to dict
    result = await users_collection.update_one({"firebase_uid": user_id}, {"$set": user_update})
    if result.modified_count:
        return await users_collection.find_one({"firebase_uid": user_id})
    else:
        raise HTTPException(status_code=404, detail="User not found")

async def delete_user(user_id: str) -> bool:
    db = get_database()
    users_collection = db["users"]
    result = await users_collection.delete_one({"firebase_uid": user_id})
    return result.deleted_count > 0


def is_superuser(user: dict) -> bool:
        return user.is_superuser