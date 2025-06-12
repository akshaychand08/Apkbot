import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
LOG_CHANNEL_ID = os.getenv("LOG_CHANNEL_ID")
ARCHIVE_CHANNEL_ID = os.getenv("ARCHIVE_CHANNEL_ID")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split()))
CREDIT = "\n\n📤 Uploaded by @iPapcorn_Prime"
