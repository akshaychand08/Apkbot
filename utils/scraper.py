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
        # APKCombo
        try:
            url = f"https://apkcombo.com/en/search/?q={query}"
            resp = await client.get(url, headers=HEADERS)
            print("APKCombo status:", resp.status_code)

            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")
                found = soup.select("a[href^='/en/'] h5")

                if not found:
                    print("❌ APKCombo: No results found.")
                else:
                    for h5 in found[:3]:
                        a_tag = h5.find_parent("a")
                        name = h5.text.strip()
                        link = "https://apkcombo.com" + a_tag["href"]
                        results.append(f"📦 {name}: {link}")
            else:
                results.append("❌ APKCombo blocked the request.")
        except Exception as e:
            results.append("APKCombo error: " + str(e))

    return results or ["❌ No results found."]
    
