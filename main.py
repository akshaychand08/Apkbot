from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN, WEBHOOK_URL
from handlers import setup_handlers
from core.mongo import init_db

def main():
    init_db()

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    setup_handlers(app)

    app.run_webhook(
        listen="0.0.0.0",
        port=8080,
        webhook_url=WEBHOOK_URL
    )

if __name__ == '__main__':
    main()
