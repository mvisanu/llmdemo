import sys
print("Python executable in use:", sys.executable)



from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

def create_simple_llm():
  """
  Creates a simpll LLM using a small GPT-2 model.
  GPT-2 (smallest version) is perfect for demonstrations as it's:
  - Relatively small (124M parameters)
  - Fast enough to run on CPU
  - Good for understanding basic concepts
  """
  # Initialize the model and tokenizer
  model_name = "distilgpt2"
  
  # Create the generator pipline
  generator = pipeline('text-generation',
                       model=model_name,
                       pad_token_id=50256)
  
  return generator


def generate_text(generator, prompt):
    result = generator(
        prompt,
        max_length=100,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.7
    )
    return result[0]["generated_text"]
  


def run_llm_demo():
  """
  Demonstrates basic LLM functionality with explanations
  """
  print(":-) Loading Simple LLM Model...")
  generator = create_simple_llm()
  
  print("\n Simple LLM Demo ")
  print("This demo shows basic text geeration using a small language model")
  
  prompts = [
    "The quick brown fox",
    "Once upon a time",
    "Python programming is",
  ]
  
  for prompt in prompts:
    print(f"\nPrompt: {prompt}")
    generated_text = generate_text(generator, prompt)
    print(f"Generated Text: {generated_text}")
    input("\nPress Enter to see next emaple...")
    
    
def interactive_demo():
  """
  Allows users to interact with the model
  """
  generator = create_simple_llm()
  
  print("\n Interactive LLM Demo")
  print("Type your prompts or 'exit' to quit")
  
  while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
      break
    
    generated_text = generate_text(generator, user_input)
    print(f"Model: {generated_text}")
    print("\n")
    
def explain_process():
  """
  Explains the process with simple examples
  """
  print("\n How it works")
  print("1. Input text -> Tokenization -> Numbers")
  print("2. Nunmbers -> Model -> Predictions")
  print("3. Predictions -> Decoding -> Text")
  
  # Simple tokenization example
  tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
  text = "Hello world!"
  tokens = tokenizer.encode(text)
  decoded = tokenizer.decode(tokens)
  
  print("\n Example Tokenization:")
  print(f"Original Text: {text}")
  print(f"As tokens (numbers): {tokens}")
  print(f"Decoded back to text: {decoded}")


if __name__ == "__main__":
  print("Choose a demo:")
  print("1. Run basic demonstration")
  print("2. Interactive demo")
  print("3. Explain process")
  
  choice = input("Enter your choice (1/2/3): ")
  
  if choice == "1":
    run_llm_demo()
  elif choice == "2":
    interactive_demo()
  elif choice == "3":
    explain_process()
  else:
    print("Invalid choice!")