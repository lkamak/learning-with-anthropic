from anthropic import Anthropic
from dotenv import load_dotenv
import base64

load_dotenv()

client = Anthropic()

research_paper_pages = [
    "./images/research_paper/page1.png",
    "./images/research_paper/page2.png",
    "./images/research_paper/page3.png",
    "./images/research_paper/page4.png",
    "./images/research_paper/page5.png"
    ]

def create_image_message(image_path): ## Reusing helper function provided in the notebook
    # Open the image file in "read binary" mode
    with open(image_path, "rb") as image_file:
        # Read the contents of the image as a bytes object
        binary_data = image_file.read()
    
    # Encode the binary data using Base64 encoding
    base64_encoded_data = base64.b64encode(binary_data)
    
    # Decode base64_encoded_data from bytes to a string
    base64_string = base64_encoded_data.decode('utf-8')
    
    # Create the image block
    image_block = {
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": "image/png",
            "data": base64_string
        }
    }
    
    return image_block

if __name__=="__main__":

    transcribed_text = ""

    for image_path in research_paper_pages:

        prompt = [
            {
                "role":"user",
                "content": [
                    create_image_message(image_path),
                    {"type":"text", "text": "Transcribe the text within this image of a research paper."}
                ]
            }
        ]

        transcription = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            messages=prompt
        )

        transcribed_text = transcribed_text + transcription.content[0].text + "\n"
        #print(transcription.content[0].text)

    paper_summary = client.messages.create(
        model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            system="You are an expert in reading scientific papers and summarizing them for non-technical audiences. Take any provided text and summarize it for the user.",
            messages=[
                {
                    "role":"user",
                    "content": [
                        {"type":"text", "text": transcribed_text}
                    ]
                }
            ]
    )

    print(paper_summary.content[0].text)