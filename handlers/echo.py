# handlers/echo.py
from telegram import Update
from telegram.ext import ContextTypes

async def echo_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    await update.message.reply_text(f"Searching for APK: {query}...\n(This feature is under development)")
  
