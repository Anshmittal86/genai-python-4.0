from openai import OpenAI
from dotenv import load_dotenv
import json
load_dotenv()

client = OpenAI()


SYSTEM_PROMPT="""
You're an expert AI Assistant in resolving user query using chain of thoughts.
You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PlAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.

RULES:-
- Strictly Follow the given JSON Format
- Only run one step at a time
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
    model="gpt-4o-mini",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": "Can You solve 2 + 3 * 6?" },
        { "role": "assistant", "content": json.dumps({ "step": "START" , "content": "Can You solve 2 + 3 * 6?" }) },
        { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "The user is requesting assistance with a mathematical expression."}) },
        { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "We need to solve this using the BODMAS method, prioritizing multiplication before addition."}) },
        { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "First, we'll perform the multiplication in the expression 3 * 6."}) },
        { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "Calculating 3 * 6 gives us 18."}) },
        { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "Now we update the expression to 2 + 18."}) },
        { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "Next, we add 2 + 18 which results in 20."}) },
        { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "Great, we have solved the expression and the final answer is 20."}) },
        { "role": "assistant", "content": json.dumps({"step": "OUTPUT", "content": "20"}) },
    ]
)

print(f"Response: {response.choices[0].message.content}")