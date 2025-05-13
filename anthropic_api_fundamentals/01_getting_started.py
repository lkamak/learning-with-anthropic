from dotenv import load_dotenv
import os
from anthropic import Anthropic

load_dotenv()
my_api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(
    api_key=my_api_key
)

joke_message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Hello, Claude! Tell me joke!"},
    ]
)

print(joke_message.content[0].text)