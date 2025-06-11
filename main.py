from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN, WEBHOOK_URL
from handlers import setup_handlers
from core.mongo import init_db

application = ApplicationBuilder().token(BOT_TOKEN).build()
setup_handlers(application)
init_db()

if __name__ == '__main__':
    application.run_webhook(
        listen="0.0.0.0",
        port=8080,
        webhook_url=WEBHOOK_URL
    )
