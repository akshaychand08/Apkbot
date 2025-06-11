from .start import start_cmd
from .ai_query import ai_query_handler
from .image import image_cmd
from telegram.ext import MessageHandler, filters

def setup_handlers(app):
    app.add_handler(start_cmd)
    app.add_handler(image_cmd)
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), ai_query_handler))
