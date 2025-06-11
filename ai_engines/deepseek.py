import httpx
from config import DEEPSEEK_KEY

async def ask_deepseek(question):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_KEY}",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": question}]
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(url, headers=headers, json=json_data)
        data = resp.json()
        return data['choices'][0]['message']['content'].strip()
