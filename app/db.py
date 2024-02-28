from motor import motor_asyncio, core
from pymongo.server_api import ServerApi
from fastapi import FastAPI
import os
from app.core.config import settings

class DataBase:
    client: motor_asyncio.AsyncIOMotorClient | None
    reddit_scheduler_db = None

db = DataBase()

def get_database() -> core.AgnosticDatabase:
    return db.reddit_scheduler_db

def connect_to_mongo():
    # Choose the database based on an environment variable
    db_url = settings.MONGO_DATABASE_URI
    db.client = motor_asyncio.AsyncIOMotorClient(db_url)
    # You might want to dynamically set the database name as well
    db_name = settings.MONGO_DATABASE_TEST
    db.reddit_scheduler_db = db.client[db_name]

def ping() :
    try:
        db.client.admin.command('ping')
        return "Pinged your deployment. You successfully connected to MongoDB!"
    except Exception as e:
        return e

def close_mongo_connection():
    db.client.close()

def create_start_app_handler(app: FastAPI) -> callable:
    def start_app() -> None:
        connect_to_mongo()
    return start_app

def create_stop_app_handler(app: FastAPI) -> callable:
    def stop_app() -> None:
        close_mongo_connection()
    return stop_app
