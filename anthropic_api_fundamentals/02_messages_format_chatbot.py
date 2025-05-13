from dotenv import load_dotenv
import os
from anthropic import Anthropic

load_dotenv()
my_api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(
    api_key=my_api_key
)

def chatbot(conversation_history=[]):
    
    done = "y"

    if len(conversation_history) > 0:
        if conversation_history[-1]['role'] == 'assitant':
            user_message = input("Your message: ")
            conversation_history.append(
                {"role": "user", "content":user_message}
            )

            chat = client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=1000,
                messages=conversation_history,
            )

            conversation_history.append({"role":chat.role, "content":chat.content[0].text})

            print(chat.content[0].text)

            done = input("Would you like to continue the conversation? (y/n): ")     

    while done == "y":
        user_message = input("Your message: ")

        conversation_history.append(
            {"role": "user", "content": user_message}
        )

        chat = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1000,
            messages=conversation_history,
        )

        print(chat.content[0].text)
        conversation_history.append({"role":chat.role, "content":chat.content[0].text})

        done = input("Would you like to continue the conversation? (y/n): ")    

if __name__=="__main__":
    chatbot()
    pass
