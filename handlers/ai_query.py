from ai_engines.chatgpt import ask_chatgpt
from ai_engines.gemini import ask_gemini
from ai_engines.deepseek import ask_deepseek
from utils.telegraph import post_to_telegraph
from config import UPDATE_CHANNEL_ID
from telegram.constants import ChatMemberStatus
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def ai_query_handler(update, context):
    user = update.effective_user
    question = update.message.text

    # Check if user is in update channel
    try:
        member = await context.bot.get_chat_member(UPDATE_CHANNEL_ID, user.id)
        if member.status in [ChatMemberStatus.LEFT, ChatMemberStatus.KICKED]:
            keyboard = [
                [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{UPDATE_CHANNEL_ID.replace('@','')}")],
                [InlineKeyboardButton("✅ I’ve Joined", callback_data="check_join")]
            ]
            await update.message.reply_text(
                "❌ Please join our update channel to use this bot.",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
            return
    except:
        await update.message.reply_text("⚠️ Couldn’t verify channel membership.")
        return

    try:
        gpt_resp = await ask_chatgpt(question)
        gemini_resp = await ask_gemini(question)
        deepseek_resp = await ask_deepseek(question)

        content = f"<b>🤖 ChatGPT:</b><br>{gpt_resp}<br><br>"
        content += f"<b>🔮 Gemini:</b><br>{gemini_resp}<br><br>"
        content += f"<b>🧠 DeepSeek:</b><br>{deepseek_resp}"

        link = post_to_telegraph(title=question, content=content)
        await update.message.reply_text(f"📄 Your Answer: {link}")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")
      
