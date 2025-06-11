from .start import start_cmd
from .image import image_cmd
from telegram.ext import MessageHandler, filters
from .ai_query import ai_query_handler

def setup_handlers(app):
    for handler in start_cmd:
        app.add_handler(handler)
    app.add_handler(image_cmd)
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), ai_query_handler))
