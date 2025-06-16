from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 नमस्कार! Welcome to the GK Quiz Bot!\n\n"
        "तयार राहा तुमच्या General Knowledge ची परीक्षा घेण्यासाठी.\n"
        "कृपया /quiz लिहा प्रश्न सुरू करण्यासाठी."
    )
