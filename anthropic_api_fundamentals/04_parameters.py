from dotenv import load_dotenv
import os
from anthropic import Anthropic

load_dotenv()
my_api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(
    api_key=my_api_key
)

def generate_question(topic, num_questions):

    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        system=f"You are an expert in the topic of {topic}. Provide only the questions, and as a numbered list.",
        stop_sequences=[str(num_questions + 1)],
        messages=[
            {"role": "user", "content": f"Generate {num_questions} thought provoking questions about {topic}"}
        ]
    )

    return message.content[0].text

if __name__=="__main__":
    
    topic = input("Write the name of a topic: ")
    num_questions = int(input("How many questions?: "))

    questions = generate_question(topic, num_questions)
    print(questions)