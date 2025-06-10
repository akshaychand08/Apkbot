from flask import Flask, request
from telegram import Bot, Update
from config import BOT_TOKEN, PORT
from bot import setup_dispatcher

app = Flask(__name__)
bot = Bot(token=BOT_TOKEN)
dispatcher = setup_dispatcher(bot)

@app.route('/')
def home():
    return "🤖 APK Bot is running!"

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
  
