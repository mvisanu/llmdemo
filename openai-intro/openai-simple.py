from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a college professor."},
        {"role": "user", "content": """write me a short essay about agentic ai. 
         write the essay in english.
         make sure to include a title.
         """},
    ]
)

print(response.choices[0].message.content)

