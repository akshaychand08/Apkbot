import httpx
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

async def search_apk(query):
    results = []

    #apkpure
    try:
        url1 = f"https://apkpure.com/search?q={query}"
        async with httpx.AsyncClient() as client:
            resp1 = await client.get(url1, headers=headers)
            if resp1.status_code == 200:
                soup1 = BeautifulSoup(resp1.text, "html.parser")
                for a in soup1.select(".search-title a")[:3]:
                    name = a.text.strip()
                    link = "https://apkpure.com" + a["href"]
                    results.append(f"📱 {name}: {link}")
    except Exception as e:
        results.append(f"APKPure error: {e}")

    #getintopc
    try:
        url2 = f"https://getintopc.com/full-search/?q={query}"
        async with httpx.AsyncClient() as client:
            resp2 = await client.get(url2, headers=headers)
            if resp2.status_code == 200:
                soup2 = BeautifulSoup(resp2.text, "html.parser")
                for a in soup2.select(".post-title a")[:2]:
                    name = a.text.strip()
                    link = a["href"]
                    results.append(f"💻 {name}: {link}")
    except Exception as e:
        results.append(f"GetIntoPC error: {e}")

    #filecr
    try:
        url3 = f"https://filecr.com/?s={query}"
        async with httpx.AsyncClient() as client:
            resp3 = await client.get(url3, headers=headers)
            if resp3.status_code == 200:
                soup3 = BeautifulSoup(resp3.text, "html.parser")
                for a in soup3.select(".post-title a")[:2]:
                    name = a.text.strip()
                    link = a["href"]
                    results.append(f"🗂️ {name}: {link}")
    except Exception as e:
        results.append(f"FileCR error: {e}")

    return results if results else ["❌ No results found."]
    
