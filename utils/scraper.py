import httpx
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/113.0.0.0 Safari/537.36"
}
async def search_apk(query):
    results = []

    async with httpx.AsyncClient() as client:
        # APKPure 
        try:
            url1 = f"https://apkpure.com/search?q={query}"
            resp1 = await client.get(url1, headers=headers)
            print("APKPure status:", resp1.status_code)
            html1 = resp1.text

            if resp1.status_code != 200:
                print("APKPure non-200 status, HTML:", html1[:500])
            else:
                # Debug first 500 characters to inspect structure
                print("APKPure HTML snippet:", html1[:500])

                soup1 = BeautifulSoup(html1, "html.parser")
                # Try multiple selectors:
                sel1 = soup1.select(".search-list .card a.title")
                sel2 = soup1.select(".search-title a")
                sel3 = soup1.select("a[href*='/'][class]")
                found = sel1 or sel2 or sel3

                if not found:
                    print("❌ APKPure: No results found. HTML snippet:", html1[:500])
                else:
                    for a in found[:3]:
                        name = a.text.strip()
                        link = "https://apkpure.com" + a["href"]
                        results.append(f"📱 {name}: {link}")
        except Exception as e:
            results.append("APKPure error: " + str(e))

        # GetIntoPC 
        try:
            url2 = f"https://getintopc.com/full-search/?q={query}"
            resp2 = await client.get(url2, headers=headers)
            print("GetIntoPC status:", resp2.status_code)

            if resp2.status_code == 200:
                soup2 = BeautifulSoup(resp2.text, "html.parser")
                found2 = soup2.select(".post-title a")
                if not found2:
                    print("❌ GetIntoPC: No results, HTML:", resp2.text[:500])
                else:
                    for a in found2[:2]:
                        results.append(f"💻 {a.text.strip()}: {a['href']}")
        except Exception as e:
            results.append("GetIntoPC error: " + str(e))

        # FileCR 
        try:
            url3 = f"https://filecr.com/?s={query}"
            resp3 = await client.get(url3, headers=headers)
            print("FileCR status:", resp3.status_code)

            if resp3.status_code == 200:
                soup3 = BeautifulSoup(resp3.text, "html.parser")
                found3 = soup3.select(".post-title a")
                if not found3:
                    print("❌ FileCR: No results, HTML:", resp3.text[:500])
                else:
                    for a in found3[:2]:
                        results.append(f"🗂️ {a.text.strip()}: {a['href']}")
        except Exception as e:
            results.append("FileCR error: " + str(e))

    return results or ["❌ No results found."]
