from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a math tutor."},
        {"role": "user", "content": """Solve this math probel step by step:. 
         If john has 3 apples and he gives 1 apple to Mary, how many apples does John have left?
          """},
    ]
)

print(completion.choices[0].message.content)