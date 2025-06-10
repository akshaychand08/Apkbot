from flask import Flask, request
from telegram.ext import Application
from config import BOT_TOKEN, WEBHOOK_URL
from handlers import setup_handlers

app = Flask(__name__)

application = Application.builder().token(BOT_TOKEN).build()
setup_handlers(application)

@app.route("/", methods=["GET"])
def index():
    return "Bot is running!"

@app.route("/", methods=["POST"])
def webhook():
    update = request.get_json(force=True)
    application.update_queue.put(update)
    return "OK"

if __name__ == "__main__":
    application.run_webhook(
        listen="0.0.0.0",
        port=8080,
        webhook_url=WEBHOOK_URL,
    )
    app.run(host="0.0.0.0", port=8080)
    
