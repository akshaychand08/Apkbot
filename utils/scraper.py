import httpx
from bs4 import BeautifulSoup

async def search_apk(query):
    results = []

    # apkpure
    url1 = f"https://apkpure.com/search?q={query}"
    async with httpx.AsyncClient() as client:
        resp1 = await client.get(url1)
        soup1 = BeautifulSoup(resp1.text, "html.parser")
        for a in soup1.select(".search-title a")[:3]:
            name = a.text.strip()
            link = "https://apkpure.com" + a["href"]
            results.append(f"📱 {name}: {link}")

    # getintopc
    url2 = f"https://getintopc.com/full-search/?q={query}"
    async with httpx.AsyncClient() as client:
        resp2 = await client.get(url2)
        soup2 = BeautifulSoup(resp2.text, "html.parser")
        for a in soup2.select(".post-title a")[:2]:
            name = a.text.strip()
            link = a["href"]
            results.append(f"💻 {name}: {link}")

    # filecr
    url3 = f"https://filecr.com/?s={query}"
    async with httpx.AsyncClient() as client:
        resp3 = await client.get(url3)
        soup3 = BeautifulSoup(resp3.text, "html.parser")
        for a in soup3.select(".post-title a")[:2]:
            name = a.text.strip()
            link = a["href"]
            results.append(f"🗂️ {name}: {link}")

    return results or ["❌ No results found."]
