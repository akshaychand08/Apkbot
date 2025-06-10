from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from core.mongo import users_col

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not users_col.find_one({"user_id": user_id}):
        users_col.insert_one({"user_id": user_id})
    await update.message.reply_text("Welcome to APKBot!")

start_cmd = CommandHandler("start", start)
