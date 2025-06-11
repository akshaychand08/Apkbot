from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
from config import OWNER_ID

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_user.id) != OWNER_ID:
        return
    message = ' '.join(context.args)
    await update.message.reply_text(f"Broadcasting: {message}")

broadcast_cmd = CommandHandler("broadcast", broadcast)
