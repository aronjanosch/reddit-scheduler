from fastapi import FastAPI
from app.db import create_start_app_handler, create_stop_app_handler, ping
from app.api.api_v1.endpoints import posts, users
from app.core.config import settings
from app.firebase_admin import initialize_firebase_admin

app = FastAPI(
    title=settings.PROJECT_NAME,
)

app.add_event_handler("startup", create_start_app_handler(app))
app.add_event_handler("shutdown", create_stop_app_handler(app))

@app.on_event("startup")
async def startup_event():
    initialize_firebase_admin()

# Register the API router
app.include_router(posts.router, prefix="/api/v1/posts", tags=["posts"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ping")
async def p():
    return {"message": ping()}
