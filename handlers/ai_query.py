from ai_engines.meta_ai import ask_meta_ai
from ai_engines.gemini import ask_gemini
from ai_engines.deepseek import ask_deepseek
from utils.telegraph import post_to_telegraph

async def ai_query_handler(update, context):
    user = update.effective_user
    question = update.message.text

    try:
        meta_resp = await ask_meta_ai(question)
        gemini_resp = await ask_gemini(question)
        deepseek_resp = await ask_deepseek(question)

        content = f"<b>🤖 Meta AI:</b><br>{meta_resp}<br><br>"
        content += f"<b>🔮 Gemini:</b><br>{gemini_resp}<br><br>"
        content += f"<b>🧠 DeepSeek:</b><br>{deepseek_resp}"

        link = post_to_telegraph(title=question, content=content)
        await update.message.reply_text(f"📄 Your Answer: {link}")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")
