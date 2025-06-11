from .start import start_cmd
from .broadcast import broadcast_cmd
from .admin import admin_cmd
from .verify import verify_middleware
from telegram.ext import MessageHandler, filters

def setup_handlers(app):
    app.add_handler(start_cmd)
    app.add_handler(broadcast_cmd)
    app.add_handler(admin_cmd)
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), verify_middleware))
