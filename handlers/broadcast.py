from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
from core.mongo import client
from config import ADMIN_IDS

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMIN_IDS:
        await update.message.reply_text("⛔ You are not authorized to use this command.")
        return

    text = update.message.text.replace("/broadcast", "").strip()
    if not text:
        await update.message.reply_text("Please provide a message to broadcast.")
        return

    db = client['ai_bot']
    users = db.users.find()
    success = 0

    for user in users:
        try:
            await context.bot.send_message(chat_id=user['_id'], text=text)
            success += 1
        except:
            continue

    await update.message.reply_text(f"✅ Broadcast sent to {success} users.")

broadcast_cmd = [
    CommandHandler("broadcast", broadcast)
]
