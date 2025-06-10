from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
from core.mongo import users_col

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != 5721673207:  # Replace with your admin ID
        return

    message = " ".join(context.args)
    if not message:
        await update.message.reply_text("Usage: /broadcast <message>")
        return

    users = users_col.find()
    for user in users:
        try:
            await context.bot.send_message(chat_id=user["user_id"], text=message)
        except Exception:
            continue

broadcast_cmd = CommandHandler("broadcast", broadcast)
