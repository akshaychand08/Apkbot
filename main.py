import logging
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from handlers import setup_handlers
from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

application = Application.builder().token(BOT_TOKEN).build()
setup_handlers(application)

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put_nowait(update)
    return "OK"

@app.route("/")
def home():
    return "Bot is running."

async def set_webhook():
    webhook_url = f"https://growing-patricia-akshaychand12-243643d5.koyeb.app/{BOT_TOKEN}"
    await application.bot.set_webhook(webhook_url)

if __name__ == "__main__":
    import asyncio
    asyncio.run(set_webhook())
    app.run(host="0.0.0.0", port=8080)
    
