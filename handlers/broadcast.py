# handlers/broadcast.py
from telegram import Update
from telegram.ext import ContextTypes
from core.mongo import users_col
import logging

logger = logging.getLogger(__name__)

OWNER_ID = 123456789  # <-- Replace with your Telegram user ID

async def broadcast_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("You are not authorized to use this command.")
        return

    if not context.args:
        await update.message.reply_text("Usage: /broadcast <message>")
        return

    message = " ".join(context.args)
    sent, failed = 0, 0

    for user in users_col.find():
        try:
            await context.bot.send_message(chat_id=user["_id"], text=message)
            sent += 1
        except Exception as e:
            logger.warning(f"Failed to send message to {user['_id']}: {e}")
            failed += 1

    await update.message.reply_text(f"Broadcast complete.\n✅ Sent: {sent}\n❌ Failed: {failed}")
