import google.generativeai as genai
from config import GEMINI_KEY

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-pro")

async def ask_gemini(question):
    response = model.generate_content(question)
    return response.text.strip()
