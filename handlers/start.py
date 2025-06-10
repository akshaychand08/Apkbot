# handlers/start.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from core.config import UPDATE_CHANNEL
from core.mongo import users_col
import logging

logger = logging.getLogger(__name__)

async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    users_col.update_one({"_id": user_id}, {"$set": dict(update.effective_user.to_dict())}, upsert=True)
    logger.info(f"User {user_id} started the bot.")

    keyboard = [[InlineKeyboardButton("Updates", url=f"https://t.me/{UPDATE_CHANNEL.lstrip('@')}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome to APKBot! Send me the name of any APK you want.",
        reply_markup=reply_markup
  )
  
