from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
from core.mongo import client

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = client['ai_bot']
    total_users = db.users.count_documents({})
    await update.message.reply_text(f"👥 Total Users: {total_users}\n✅ Bot is working fine!")

stats_cmd = [
    CommandHandler("status", stats),
    CommandHandler("users", stats)
]
