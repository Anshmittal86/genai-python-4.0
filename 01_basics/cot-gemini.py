from openai import OpenAI
from dotenv import load_dotenv
import json
load_dotenv()

client = OpenAI(
    api_key="GEMINI_API_KEY_PASTE_HERE",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


SYSTEM_PROMPT="""
You're an expert AI Assistant in resolving user query using chain of thoughts.
You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PlAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.

RULES:-
- Strictly Follow the given JSON Format
- Only run one step at a time in every situation gives only and only one step (Very Strictly)
- The sequence of step is START (Where user gives an INPUT), PLAN(That can be multiple time) and finally OUTPUT(which is going to the displayed to the user.)

OUTPUT JSON Format:- 
{ "step": "START" | "PLAN" | "OUTPUT", "content": string }


Example:
Q: Hey, Can you solve 2 + 3 * 10 / 2?
Answer: 
START: { "step": "START" , "content": "Hey, Can you solve 2 + 3 * 10 / 2?" }
PLAN: { "step": "PLAN" , "content": "Seems, like user is interested in math problem." }
PLAN: { "step": "PLAN" , "content": "looking at the problem, we should solve this using BODMAS method." }
PLAN: { "step": "PLAN" , "content": "Yes, The BODMAS is correct think to done here." }
PLAN: { "step": "PLAN" , "content": "first we must Divide the 10 / 2 which is 5." }
PLAN: { "step": "PLAN" , "content": "Now the new equation is 2 + 3 * 5" }
PLAN: { "step": "PLAN" , "content": "Now, we must multiply 3 * 5 which is 15." }
PLAN: { "step": "PLAN" , "content": "Now, the equation is 2 + 15" }
PLAN: { "step": "PLAN" , "content": "Now, finally lets perform the addition of 2 + 15 which is 17." }
PLAN: { "step": "PLAN" , "content": "Great, we have solved and finally left with 17 as answer." }
OUTPUT: { "step": "OUTPUT" , "content": "17" }
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": "Can You solve 2 + 3 * 6?" },
        { "role": "user", "content": json.dumps({ "step": "START" , "content": "Can You solve 2 + 3 * 6?" }) },
        { "role": "user", "content": json.dumps({ "step": "PLAN", "content": "The user wants to solve a mathematical expression: 2 + 3 * 6." }) },
        { "role": "user", "content": json.dumps({"step": "PLAN", "content": "According to the order of operations (BODMAS/PEMDAS), multiplication should be performed before addition."}) },
        { "role": "user", "content": json.dumps({ "step": "PLAN", "content": "First, calculate 3 * 6." }) },
        { "role": "user", "content": json.dumps({ "step": "PLAN", "content": "3 * 6 equals 18." }) },
        { "role": "user", "content": json.dumps({"step": "PLAN", "content": "Now, substitute the result back into the expression: 2 + 18."}) },
        { "role": "user", "content": json.dumps({"step": "PLAN", "content": "Finally, calculate 2 + 18."}) },
        { "role": "user", "content": json.dumps({ "step": "PLAN", "content": "2 + 18 equals 20." }) },
        { "role": "user", "content": json.dumps({"step": "OUTPUT", "content": "20"}) },
        
    ]
)

print(f"Response: {response.choices[0].message.content}")