import httpx
import os
from config import META_AI_KEY, META_AI_URL

async def ask_meta_ai(prompt):
    headers = {
        "Authorization": f"Bearer {META_AI_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(META_AI_URL, headers=headers, json=data)
        result = response.json()
        return result['choices'][0]['message']['content']
