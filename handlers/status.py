# handlers/status.py
from telegram import Update
from telegram.ext import ContextTypes
from core.mongo import users_col

async def status_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    count = users_col.count_documents({})
    await update.message.reply_text(f"Bot is running.\nTotal users: {count}")
  
