from telegram.ext import CommandHandler
from telegram import Update
import openai
from config import IMAGE_LIMIT_PER_DAY
from core.mongo import get_user_data, increment_image_count

openai.api_key = "sk-placeholder"  # remove or replace if not using

async def generate_image(prompt):
    return "https://dummyimage.com/512x512/000/fff&text=Generated+Image"

async def image(update: Update, context):
    prompt = ' '.join(context.args)
    if not prompt:
        await update.message.reply_text("❗ Usage: /image your prompt here")
        return

    user_id = update.effective_user.id
    usage = get_user_data(user_id)
    if usage['count'] >= IMAGE_LIMIT_PER_DAY:
        await update.message.reply_text("❌ Daily image limit reached. Try again tomorrow or upgrade your plan.")
        return

    url = await generate_image(prompt)
    increment_image_count(user_id)
    await update.message.reply_photo(url, caption=f"🖼️ Generated for: {prompt}")

image_cmd = CommandHandler("image", image)
