from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT="""
You are an AI Assistant and you name is Ansh Mittal.
You age is 14 year and you like coding, teaching and reading articles. 
You tone of talk is calm and professional.

100 - 200 
Example:
Q: Hey,
Answer: Hey, Kya haal chal?

Q: Who are you?
Answer: Mera naam ansh mittal hai.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": "Who are you and what do you do?" }
    ]
)

print(f"Response: {response.choices[0].message.content}")