import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

MODEL_NAME = "gemini-3.1-flash-lite"

client = genai.Client(api_key=API_KEY)