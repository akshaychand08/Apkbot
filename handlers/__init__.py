from .media import media_handler, quality_handler
from .pdf_converter import photo_to_pdf, pdf_to_photo
from .start import start_cmd
from .stats import stats_cmd
from .broadcast import broadcast_cmd
from telegram.ext import MessageHandler, CommandHandler, CallbackQueryHandler, filters

def setup_handlers(app):
    for handler in start_cmd + stats_cmd + broadcast_cmd:
        app.add_handler(handler)
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), media_handler))
    app.add_handler(CallbackQueryHandler(quality_handler, pattern="^video_"))
    app.add_handler(CommandHandler("photo2pdf", photo_to_pdf))
    app.add_handler(CommandHandler("pdf2photo", pdf_to_photo))
