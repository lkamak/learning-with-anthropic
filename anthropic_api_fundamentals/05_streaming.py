from anthropic import AsyncAnthropic, AsyncMessageStream
import asyncio
from dotenv import load_dotenv

load_dotenv()

client = AsyncAnthropic()

green = '\033[32m'
blue = '\033[34m'
reset = '\033[0m'

async def start_session():
    
    conversation_history = []

    print("Starting session. Write 'quit' to exit.")

    while True:

        user_prompt = input(blue + "You: " + reset)
        if user_prompt.lower() == "quit":
            break

        conversation_history.append(
            {
                "role":"user",
                "content":user_prompt
            }
        )

        async with client.messages.stream(
            max_tokens=1024,
            system="You are a friendly chatbot. Interact with the user based on their requirements, but be succint in your answers.",
            messages=conversation_history,
            model="claude-3-haiku-20240307",
            temperature=1
        ) as stream:
            print(green + "Claude: " + reset, end="")
            async for event in stream:
                if event.type == "text":
                    print(green + event.text + reset, end="", flush=True)
        
        final_message = await stream.get_final_message()
        conversation_history.append({"role":"assistant", "content":final_message.content[0].text})
        print("\n", end="")
        
if __name__=="__main__":
    asyncio.run(start_session())