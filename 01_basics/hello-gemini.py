from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key="GEMINI_API_KEY_PASTE_HERE",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        { "role": "system", "content": "You are helpful AI Assistant." },
        { "role": "user", "content": "Hello Kya haal chal?" }
    ]
)

print(f"Response: {response.choices[0].message.content}")