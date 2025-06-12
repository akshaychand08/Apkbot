from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.downloader import get_video_formats, download_video_by_format
from config import CREDIT, ARCHIVE_CHANNEL_ID
import os

async def media_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if any(site in text for site in ["youtube.com", "youtu.be"]):
        await update.message.reply_text("🔍 Fetching available formats...")
        formats = get_video_formats(text)

        if not formats:
            await update.message.reply_text("❌ No formats found.")
            return

        buttons = [[InlineKeyboardButton(f"🎞 {fmt['format_note']}", callback_data=f"video_{fmt['format_id']}|{text}")]
                   for fmt in formats if fmt['ext'] == 'mp4' and fmt.get('format_note')]

        await update.message.reply_text("🎬 Choose a video quality:", reply_markup=InlineKeyboardMarkup(buttons))

async def quality_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data.replace("video_", "")
    fmt_id, url = data.split("|", 1)

    await query.edit_message_text("⬇ Downloading your selected quality...")
    results = await download_video_by_format(url, fmt_id)

    for file in results:
        if file.endswith(".mp4"):
            await query.message.reply_video(video=open(file, 'rb'), caption=CREDIT)
            await context.bot.send_video(chat_id=ARCHIVE_CHANNEL_ID, video=open(file, 'rb'),
                                         caption=f"📤 by @{query.from_user.username} ({query.from_user.id})")
            os.remove(file)
        else:
            await query.message.reply_text(file)
          
