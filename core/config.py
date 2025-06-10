# core/config.py
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
MONGO_URI = os.environ.get("MONGO_URI", "YOUR_MONGO_URI")
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "@YourLogChannel")
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "@YourUpdateChannel")
OWNER_ID = int(os.environ.get("OWNER_ID", "123456789"))
