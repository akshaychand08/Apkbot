import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("7823889476:AAFnvcNQ1ptmshYLYhQbm2lPpkGqfb2BDZs")
WEBHOOK_URL = os.getenv("https://growing-patricia-akshaychand12-243643d5.koyeb.app")
LOG_CHANNEL_ID = os.getenv("-1002772843586")
ARCHIVE_CHANNEL_ID = os.getenv("-1002772843586")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "5721673207").split()))
CREDIT = "\n\n📤 Uploaded by @iPapcorn_Prime"
