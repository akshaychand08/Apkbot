from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, Filters, Dispatcher
import requests
from bs4 import BeautifulSoup

def start(update, context):
    update.message.reply_text("🤖 Welcome to the All-in-One APK Bot!\nType any app name to search.")

def search_apk(update, context):
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
            update.message.reply_text(r, disable_web_page_preview=True)
    else:
        update.message.reply_text("❌ Nothing found.")

def setup_dispatcher(bot):
    dp = Dispatcher(bot, None, workers=0, use_context=True)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, search_apk))
    return dp
  
