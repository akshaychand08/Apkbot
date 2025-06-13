import os
from dotenv import load_dotenv

# Load .env file if running locally
load_dotenv()

# Load sensitive keys from environment
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
LOG_CHANNEL_ID = os.getenv("LOG_CHANNEL_ID")
ARCHIVE_CHANNEL_ID = os.getenv("ARCHIVE_CHANNEL_ID")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split()))

CREDIT = "\n\n📤 Uploaded by @iPapcorn_Prime"

# Validate critical values
if not BOT_TOKEN or ":" not in BOT_TOKEN:
    raise ValueError("❌ Invalid BOT_TOKEN. Set a correct token in your Koyeb environment.")

if not WEBHOOK_URL:
    raise ValueError("❌ WEBHOOK_URL is missing. Set it in your Koyeb environment.")
