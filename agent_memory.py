from smolagents import InferenceClientModel, CodeAgent
from huggingface_hub import login
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Access the token
token = os.getenv("HUGGINGFACE_TOKEN")

print("Token loaded:", token[:5], "...")


if not token:
    raise ValueError("HUGGINGFACE_TOKEN environment variable not set. Please set it before running the script.")

login(token=token)

model = InferenceClientModel()
agent = CodeAgent(tools=[], model=model, verbosity_level=0)

result = agent.run("What's the 20th Fibonacci number?")
print("Result:", result)