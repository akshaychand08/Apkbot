from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from config import LOG_CHANNEL_ID, UPDATE_CHANNEL_ID

async def start(update, context):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("ℹ️ About", callback_data="about")],
        [InlineKeyboardButton("🚀 Bot Features", callback_data="features")],
        [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{UPDATE_CHANNEL_ID.replace('@', '')}")]
    ]
    await update.message.reply_text(
        "👋 Welcome to the Ultimate AI Bot!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    try:
        log_msg = f"👤 User Started: @{user.username or 'NoUsername'} ({user.id})"
        await context.bot.send_message(chat_id=LOG_CHANNEL_ID, text=log_msg)
    except Exception:
        pass

async def callback_handler(update, context):
    query = update.callback_query
    await query.answer()
    if query.data == "about":
        await query.edit_message_text("🤖 *About Bot:* This bot uses ChatGPT, Gemini, and DeepSeek to answer your questions and generate images.", parse_mode="Markdown")
    elif query.data == "features":
        await query.edit_message_text("🚀 *Features:*\n- Ask anything\n- AI comparison\n- Image generation\n- Telegraph answers\n- Usage limits & tracking", parse_mode="Markdown")

start_cmd = [
    CommandHandler("start", start),
    CallbackQueryHandler(callback_handler)
]
