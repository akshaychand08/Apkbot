from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton("ℹ️ About", callback_data="about")],
        [InlineKeyboardButton("🚀 Features", callback_data="features")],
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    await update.message.reply_text(
        "👋 Welcome to the Media & PDF Bot!\nUse the menu below to explore:",
        reply_markup=keyboard
    )

async def start_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "about":
        await query.edit_message_text(
            "📦 This bot lets you:\n- Convert photos to PDF\n- Convert PDF to photos\n- Download high-quality videos\n\nEnjoy!",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="start"), InlineKeyboardButton("❌ Close", callback_data="close")]])
        )
    elif query.data == "features":
        await query.edit_message_text(
            "🚀 Features:\n- YouTube/FB/Instagram download\n- PDF conversion\n- Archive uploads\n- Broadcast to users",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="start"), InlineKeyboardButton("❌ Close", callback_data="close")]])
        )
    elif query.data == "start":
        await start(update, context)
    elif query.data == "close":
        await query.delete_message()

start_cmd = [
    CommandHandler("start", start),
]
