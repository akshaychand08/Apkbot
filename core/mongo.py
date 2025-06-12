import os
from pymongo import MongoClient
from config import MONGO_URL
from datetime import datetime

client = None

def init_db():
    global client
    client = MongoClient(MONGO_URL)

def get_user_data(user_id):
    db = client['ai_bot']
    user = db.users.find_one({"_id": user_id})
    today = datetime.utcnow().date()
    if not user or user.get('last_used') != str(today):
        db.users.update_one({"_id": user_id}, {"$set": {"count": 0, "last_used": str(today)}}, upsert=True)
        return {"count": 0, "last_used": str(today)}
    return user

def increment_image_count(user_id):
    db = client['ai_bot']
    db.users.update_one({"_id": user_id}, {"$inc": {"count": 1}})
