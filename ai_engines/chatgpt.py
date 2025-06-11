import openai
from config import OPENAI_KEY

openai.api_key = OPENAI_KEY

async def ask_chatgpt(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    return response['choices'][0]['message']['content'].strip()
