# handlers/__init__.py
from telegram.ext import CommandHandler, MessageHandler, filters

from .start import start_cmd
from .broadcast import broadcast_cmd
from .status import status_cmd
from .echo import echo_msg

def setup_handlers(app):
    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(CommandHandler("broadcast", broadcast_cmd))
    app.add_handler(CommandHandler("status", status_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_msg))
  
