import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder
from bot import setup_dispatcher

# ✅ Safely get from environment
BOT_TOKEN = os.environ.get("7823889476:AAFfu6gnn91hhlcrQdrYe2z6nqt7d9iBanc")
PORT = int(os.environ.get("PORT", 8080))

if not BOT_TOKEN:
    raise ValueError("🚨 BOT_TOKEN not set! Add it as an environment variable.")

# Setup app
app = Flask(__name__)
application = ApplicationBuilder().token(BOT_TOKEN).build()
setup_dispatcher(application)

@app.route('/')
def home():
    return "🤖 APK Bot is running!"

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put_nowait(update)
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
