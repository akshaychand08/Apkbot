from pymongo import MongoClient
import os

client = None

def init_db():
    global client
    mongo_url = os.getenv("MONGO_URL", "mongodb+srv://AKirtibot:AKirtibot@cluster0.qtmdhrz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    client = MongoClient(mongo_url)

# Call immediately
init_db()
