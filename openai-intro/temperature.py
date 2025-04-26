from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a creative writer."},
        {"role": "user", "content": """Write a creative story about a time traveler who visits the year 3000.
          The story should include elements of adventure and discovery.
          """},
    ],
     temperature=0.7,
    top_p=0.9,  # Adjusting the temperature to 0.5 for more focused responses 
)

print(completion.choices[0].message.content)