import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder
from bot import setup_dispatcher

BOT_TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 8080))

if not BOT_TOKEN:
    raise ValueError("🚨 BOT_TOKEN not set! Add it as an environment variable.")

app = Flask(__name__)
application = ApplicationBuilder().token(BOT_TOKEN).build()
setup_dispatcher(application)

# ✅ Set the webhook
application.bot.set_webhook(url=f"https://growing-patricia-akshaychand12-243643d5.koyeb.app/{BOT_TOKEN}")

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
    
