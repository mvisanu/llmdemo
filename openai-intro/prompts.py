from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a translator."},
        {"role": "user", "content": """Translate these sentences:. 
         'Hello' -> 'Hola',
          'Goodbye' -> 'Adiós',
         Now translate: 'How much money do you make?'.
         """},
    ]
)

print(completion.choices[0].message.content)

# Direct prompt example with OpenAi
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": """What is the capital of France?"""},         
    ]
)

print(completion.choices[0].message.content)