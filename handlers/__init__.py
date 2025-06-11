from .start import start_cmd  # this is a LIST
from .ai_query import ai_query_handler
from .image import image_cmd
from telegram.ext import MessageHandler, filters

def setup_handlers(app):
    # Register each handler in the list
    for handler in start_cmd:
        app.add_handler(handler)

    # Register single handlers directly
    app.add_handler(image_cmd)
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), ai_query_handler))
