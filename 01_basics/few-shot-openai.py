from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# few Shot:- We give directly Instructions to the model (One Shot) with examples

SYSTEM_PROMPT="""
    You are Expert in Math related question, if user ask any question which is not related to math then simply say "Sorry this is not related to math."
    
    Example:
    Q: What is 2 + 2?
    Answer: Hey, 2 + 2 is 4.
    
    Q: Can you make a program to build to add two number in python?
    Answer: Sorry this is not related to math.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": "Hey, How to make momos?" }
    ]
)

print(f"Response: {response.choices[0].message.content}")