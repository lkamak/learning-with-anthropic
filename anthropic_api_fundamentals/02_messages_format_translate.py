from dotenv import load_dotenv
import os
from anthropic import Anthropic

load_dotenv()
my_api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(
    api_key=my_api_key
)

def translate(word, language):

    prompt = f"Please translate {word} into {language}. Return just the translated word."

    translation_request = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        messages=[
        {"role": "user", "content": prompt}],
    )

    return translation_request.content[0].text

if __name__=="__main__":

    word = "fish"
    language = "portuguese"

    translated_word = translate(word, language)

    print(translated_word)