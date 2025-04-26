from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a philosopher."},
        {"role": "user", "content": """What is the meaning of life?
          """},
    ]
)

print(completion.choices[0].message.content)