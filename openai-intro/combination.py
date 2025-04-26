from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a travel blogger."},
        {"role": "user", "content": """Write a 500-word blog post about your recent trip to bangkok. 
         Make sure to give a step by step of itenary and include some travel tips.
         Use bullet points to summarize the main points.
          """},
    ],
    temperature=0.7,
    top_p=0.9,  # Adjusting the temperature to 0.5 for more focused responses 
)

print(completion.choices[0].message.content)