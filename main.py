# main.py
from flask import Flask, request
from telegram import Update
from telegram.ext import Application
import logging

from core.config import BOT_TOKEN
from handlers import setup_handlers

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Flask
app = Flask(__name__)

# Telegram bot app
application = Application.builder().token(BOT_TOKEN).build()
setup_handlers(application)

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put_nowait(update)
    return "OK"

@app.route("/")
def index():
    return "Bot is running."

if __name__ == '__main__':
    import asyncio

    async def run():
        await application.bot.set_webhook(f"https://your-koyeb-app.koyeb.app/{BOT_TOKEN}")
        await application.initialize()
        await application.start()
        app.run(host="0.0.0.0", port=8080)

    asyncio.run(run())
