# utils/scraper.py
import httpx
from bs4 import BeautifulSoup
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

async def search_apk(query):
    results = []
    buttons = []

    # APKPure
    url_apkpure = f"https://apkpure.com/search?q={query}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url_apkpure)
        soup = BeautifulSoup(resp.text, "html.parser")
        for a in soup.select(".search-title a")[:3]:
            name = a.text.strip()
            link = "https://apkpure.com" + a["href"]
            buttons.append([InlineKeyboardButton(name, url=link)])

    # FileCR
    url_filecr = f"https://filecr.com/?s={query}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url_filecr)
        soup = BeautifulSoup(resp.text, "html.parser")
        for a in soup.select(".post-box-title a")[:3]:
            name = a.text.strip()
            link = a["href"]
            buttons.append([InlineKeyboardButton(name, url=link)])

    # GetIntoPC
    url_getinto = f"https://getintopc.com/?s={query}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url_getinto)
        soup = BeautifulSoup(resp.text, "html.parser")
        for a in soup.select("h2.post-box-title a")[:3]:
            name = a.text.strip()
            link = a["href"]
            buttons.append([InlineKeyboardButton(name, url=link)])

    if not buttons:
        return ["No results found."], None

    return ["🔍 Search Results:"], InlineKeyboardMarkup(buttons)
  
