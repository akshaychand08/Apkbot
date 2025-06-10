import os
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder
from bot import setup_dispatcher

BOT_TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 8080))
APP_URL = os.environ.get("APP_URL")  # e.g., https://yourapp.koyeb.app

if not BOT_TOKEN:
    raise ValueError("🚨 BOT_TOKEN not set! Add it as an environment variable.")

if not APP_URL:
    raise ValueError("🚨 APP_URL not set! Add it as an environment variable.")

# Flask setup
app = Flask(__name__)

# Telegram application setup
application = ApplicationBuilder().token(BOT_TOKEN).build()
setup_dispatcher(application)

@app.route('/')
def home():
    return "🤖 APK Bot is running!"

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
async def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return "OK", 200

async def set_webhook():
    await application.bot.set_webhook(url=f"{APP_URL}/{BOT_TOKEN}")

if __name__ == '__main__':
    # Set webhook before running the server
    asyncio.run(set_webhook())
    app.run(host='0.0.0.0', port=PORT)
