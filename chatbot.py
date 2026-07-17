from config import client, MODEL_NAME
from google.genai.errors import ClientError, ServerError
import time

# Stores complete conversation
chat_history = []


def get_ai_response(prompt):
    global chat_history

    # Store user message
    chat_history.append(
        {
            "role": "user",
            "parts": [{"text": prompt}]
        }
    )

    max_retries = 3

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=chat_history
            )

            # Store AI response
            chat_history.append(
                {
                    "role": "model",
                    "parts": [{"text": response.text}]
                }
            )

            return response.text

        except ServerError:
            if attempt < max_retries - 1:
                print(f"Server busy. Retrying ({attempt+1}/{max_retries})...")
                time.sleep(2)
            else:
                return "Gemini servers are busy. Please try again later."

        except ClientError as e:
            return f"Client Error:\n{e}"

        except Exception as e:
            return f"Unexpected Error:\n{e}"


def clear_chat():
    """Clear chat history"""
    global chat_history
    chat_history.clear()