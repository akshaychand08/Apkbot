from telegram.ext import CommandHandler
from config import UPDATE_CHANNEL_ID

async def start(update, context):
    user = update.effective_user
    await update.message.reply_text(
        f"👋 Hello {user.first_name}!\n\n💡 I can help you search APK files. Just send me the app name.\n📢 Join our update channel: {UPDATE_CHANNEL_ID}"
    )

start_cmd = CommandHandler("start", start)
