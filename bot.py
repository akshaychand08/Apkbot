from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, Dispatcher, ContextTypes
import requests
from bs4 import BeautifulSoup

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Welcome to the All-in-One APK Bot!\nType any app name to search.")

# Main search logic
async def search_apk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    results = []

    # APKPure
    try:
        url = f"https://apkpure.com/search?q={query.replace(' ', '+')}"
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        items = soup.find_all('div', class_='search-dl')[:2]
        for res in items:
            title = res.find('p').text.strip()
            link = "https://apkpure.com" + res.find('a')['href']
            results.append(f"📦 [APKPure] {title}\n🔗 {link}")
    except:
        pass

    # FileCR
    try:
        url = f"https://filecr.com/en/?s={query.replace(' ', '+')}"
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        for a in soup.select('.title > a')[:2]:
            results.append(f"📁 [FileCR] {a.text.strip()}\n🔗 {a['href']}")
    except:
        pass

    # GetIntoPC
    try:
        url = f"https://getintopc.com/?s={query.replace(' ', '+')}"
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        for a in soup.select('.post-title > a')[:2]:
            results.append(f"🖥️ [GetIntoPC] {a.text.strip()}\n🔗 {a['href']}")
    except:
        pass

    if results:
        for r in results:
            await update.message.reply_text(r, disable_web_page_preview=True)
    else:
        await update.message.reply_text("❌ Nothing found.")

# Dispatcher setup
def setup_dispatcher(application):
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_apk))
    return application
    
