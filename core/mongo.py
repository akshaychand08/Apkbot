# core/mongo.py
from pymongo import MongoClient
from core.config import MONGO_URI

mongo = MongoClient(MONGO_URI)
db = mongo.botdb
users_col = db.users
