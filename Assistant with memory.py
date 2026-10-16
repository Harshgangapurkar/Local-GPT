
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("="*40)
print(" MY AI ASSISTANT")
print("="*40)

messages = [] 

while True:

    user_input = input("\nYou: ")
    messages.append({"role": "user", "content": user_input})
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Goodbye!, see you next time!")
        break
    response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=messages

)

    ai_reply = response.choices[0].message.content
    print(f"AI: {ai_reply}")






