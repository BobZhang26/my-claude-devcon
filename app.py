import os
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

response = client.messages.create(
    model="Claude Sonnet 3.5 2024-10-22",
    max_tokens=100,
    temperature=0.5,
    messages=[
        {"role": "user", "content": "Explain the Turing test in simple terms."}
    ]
)

print(response.content[0]["text"])
