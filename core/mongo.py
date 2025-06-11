from pymongo import MongoClient
import os

client = None

def init_db():
    global client
    mongo_url = os.getenv("MONGO_URL", "mongodb+srv://iPapcorn:iPapcorn@cluster0.52lnvxn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    client = MongoClient(mongo_url)
