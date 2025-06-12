from telegram import Update
from telegram.ext import ContextTypes
from config import ARCHIVE_CHANNEL_ID, CREDIT

async def photo_to_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.photo:
        await update.message.reply_text("❌ Please send a photo with the /photo2pdf command.")
        return

    photo = update.message.photo[-1]
    file = await photo.get_file()
    file_path = await file.download_to_drive()

    pdf_path = file_path.replace(".jpg", ".pdf").replace(".jpeg", ".pdf").replace(".png", ".pdf")
    from PIL import Image
    image = Image.open(file_path).convert("RGB")
    image.save(pdf_path)

    await update.message.reply_document(document=open(pdf_path, 'rb'), caption=CREDIT)
    await context.bot.send_document(chat_id=ARCHIVE_CHANNEL_ID, document=open(pdf_path, 'rb'),
                                    caption=f"📤 by @{update.effective_user.username} ({update.effective_user.id})")

async def pdf_to_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.document or not update.message.document.file_name.endswith(".pdf"):
        await update.message.reply_text("❌ Please send a PDF with the /pdf2photo command.")
        return

    file = await update.message.document.get_file()
    file_path = await file.download_to_drive()

    from pdf2image import convert_from_path
    images = convert_from_path(file_path)
    for idx, img in enumerate(images):
        img_path = f"{file_path}_{idx}.jpg"
        img.save(img_path, "JPEG")
        await update.message.reply_photo(photo=open(img_path, 'rb'), caption=CREDIT)
        await context.bot.send_photo(chat_id=ARCHIVE_CHANNEL_ID, photo=open(img_path, 'rb'),
                                     caption=f"📤 by @{update.effective_user.username} ({update.effective_user.id})")
