import os
from dotenv import load_dotenv

load_dotenv()

# Load variables from .env file if present (for local dev)

# Telegram Bot
BOT_TOKEN = os.getenv("BOT_TOKEN", "7823889476:AAFnvcNQ1ptmshYLYhQbm2lPpkGqfb2BDZs")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://growing-patricia-akshaychand12-243643d5.koyeb.app")

#META_AI_KEY = os.getenv("META_AI_KEY", "your-meta-api-key")
#META_AI_URL = os.getenv("META_AI_URL", "https://your-meta-endpoint.com/v1/chat/completions")

# Gemini / Google Generative AI
GEMINI_KEY = os.getenv("GEMINI_KEY", "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")

# DeepSeek
DEEPSEEK_KEY = os.getenv("DEEPSEEK_KEY", "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")

# MongoDB
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://iPapcorn:iPapcorn@cluster0.52lnvxn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Bot Control
LOG_CHANNEL_ID = os.getenv("LOG_CHANNEL_ID", "-1002138727373")
IMAGE_LIMIT_PER_DAY = int(os.getenv("IMAGE_LIMIT_PER_DAY", "5"))
