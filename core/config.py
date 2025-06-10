# core/config.py
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7823889476:AAFfu6gnn91hhlcrQdrYe2z6nqt7d9iBanc")
MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://iPapcorn:iPapcorn@cluster0.52lnvxn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "@iPapcorn_Prime")
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "@iPapcorn_Prime")
OWNER_ID = int(os.environ.get("OWNER_ID", "5721673207"))
