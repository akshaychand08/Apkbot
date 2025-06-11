from config import UPDATE_CHANNEL_ID, LOG_CHANNEL_ID
from telegram.constants import ChatMemberStatus
from core.mongo import client
from utils.scraper import search_apk

async def verify_middleware(update, context):
    user = update.effective_user
    chat_id = update.effective_chat.id
    member = await context.bot.get_chat_member(UPDATE_CHANNEL_ID, user.id)

    if member.status in [ChatMemberStatus.LEFT, ChatMemberStatus.BANNED]:
        await update.message.reply_text("🚫 Please join our update channel first!")
        return

    if client is None:
        await update.message.reply_text("❌ Database not initialized.")
        return

    db = client['apkbot']
    db.users.update_one({'user_id': user.id}, {'$set': {'username': user.username}}, upsert=True)

    results = await search_apk(update.message.text)
    await update.message.reply_text("\n".join(results))

    await context.bot.send_message(LOG_CHANNEL_ID, f"🔎 {user.username} searched: {update.message.text}")
