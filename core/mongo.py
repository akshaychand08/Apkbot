from pymongo import MongoClient
from config import os

MONGO_URL = os.getenv("MONGO_URL")
client = None

def init_db():
    global client
    client = MongoClient(MONGO_URL)

def get_user_data(user_id):
    db = client['ai_bot']
    user = db.users.find_one({"_id": user_id})
    return user

def save_user(user_id, username):
    db = client['ai_bot']
    db.users.update_one(
        {"_id": user_id},
        {"$set": {"username": username}},
        upsert=True
    )
