import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = api_key)
MODEL_NAME = "gemini-3.5-flash"

print("=" * 50)
print("SIMPLE AI CHATBOT")
print("Type `Exit` to quite the bot")
print("="*50)

while True:
    user_input = input("\nYou: ")

    if user_input.lower()=="exit":
        print("AI: Goodbye!👋, Nice to talk with you.")
        break

    if not user_input.strip():
        print("AI: Please enter a message!.")
        continue

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=user_input
    )

    print(f"AI: {response.text}")