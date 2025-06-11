from telegram.ext import CommandHandler
from telegram import Update
from config import OWNER_ID
from core.mongo import client

async def admin(update: Update, context):
    if str(update.effective_user.id) != OWNER_ID:
        return
    if client is None:
        await update.message.reply_text("❌ Database not initialized.")
        return
    db = client['apkbot']
    user_count = db.users.count_documents({})
    await update.message.reply_text(f"👑 Admin Panel:\nTotal Users: {user_count}")

admin_cmd = CommandHandler("admin", admin)
