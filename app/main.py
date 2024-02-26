from fastapi import FastAPI
from app.db import create_start_app_handler, create_stop_app_handler, ping
from app.api.api_v1.endpoints import posts as posts_router

app = FastAPI()

app.add_event_handler("startup", create_start_app_handler(app))
app.add_event_handler("shutdown", create_stop_app_handler(app))

# Register the API router
app.include_router(posts_router.router, prefix="/api/v1/posts", tags=["posts"])

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ping")
async def p():
    return {"message": ping()}
