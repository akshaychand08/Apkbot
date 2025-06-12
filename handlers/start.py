from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from config import LOG_CHANNEL_ID

async def start(update, context):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("ℹ️ About", callback_data="about")],
        [InlineKeyboardButton("🚀 Bot Features", callback_data="features")]
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
        keyboard = [
            [InlineKeyboardButton("🔙 Back", callback_data="back"), InlineKeyboardButton("❌ Close", callback_data="close")]
        ]
        await query.edit_message_text(
            "🤖 *About Bot:* This bot uses Meta AI, Gemini, and DeepSeek to answer your questions and generate images.",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )

    elif query.data == "features":
        keyboard = [
            [InlineKeyboardButton("🔙 Back", callback_data="back"), InlineKeyboardButton("❌ Close", callback_data="close")]
        ]
        await query.edit_message_text(
            "🚀 *Features:*\n- Ask anything\n- AI comparison\n- Image generation\n- Telegraph answers\n- Usage limits & tracking",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )

    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("ℹ️ About", callback_data="about")],
            [InlineKeyboardButton("🚀 Bot Features", callback_data="features")]
        ]
        await query.edit_message_text(
            "👋 Welcome to the Ultimate AI Bot!",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "close":
        await query.delete_message()

start_cmd = [
    CommandHandler("start", start),
    CallbackQueryHandler(callback_handler)
]
