from fastapi import APIRouter, HTTPException, Body, status, Depends
from app.dependencies import get_current_user, get_current_active_superuser
from app.schemas import UserCreate, UserUpdate, UserDB
from app.crud import create_user, update_user, delete_user

router = APIRouter()

@router.post("/", response_model=UserDB)
async def create_user_data(user_data: UserCreate = Body(...), firebase_user: dict = Depends(get_current_user)):
    # Extract email from the decoded Firebase token
    email = firebase_user.get("email")
    if not email:
        raise HTTPException(status_code=400, detail="Email is required")

    # Combine the extracted email with the rest of the user data
    user_data_with_email = user_data.model_dump()
    user_data_with_email["email"] = email

    created_user = await create_user(user_data_with_email)
    return created_user

@router.patch("/", response_model=UserDB)
async def update_user_data(user_update: UserUpdate = Body(...), firebase_user: dict = Depends(get_current_user)):
    updated_user = await update_user(user_update, firebase_user['uid'])
    return updated_user

@router.delete("/{user_id}")
async def delete_user_data(firebase_user: dict = Depends(get_current_active_superuser)):
    await delete_user(firebase_user['uid'])
    return {"message": "User deleted successfully"}