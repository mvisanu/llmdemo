from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a knowledgeable personal trainer and a writer."},
        {"role": "user", "content": """Write 300-word summary of exercise, using bullet points:. 
        
          """},
    ]
)

print(completion.choices[0].message.content)