import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = "You are a fictional Indian cricket captain named Virat Kohli. You love chasing targets, are intensely competitive, and speak with confidence and energy."
client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))
message = client.messages.create(
    model= "claude-sonnet-4-20250514",
    max_tokens= 1024,
    system = SYSTEM_PROMPT,
    messages=[
        {"role": "user", "content": "Yaar, how did you feel after winning the World Cup?"}
    ]
)

print(message.content[0].text)
