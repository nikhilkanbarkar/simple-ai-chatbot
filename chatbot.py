from config import client, MODEL_NAME
from google.genai.errors import ClientError, ServerError

# Stores the complete conversation
chat_history = []


def get_ai_response(prompt):
    global chat_history

    # Store user's message
    chat_history.append(
        {
            "role": "user",
            "parts": [{"text": prompt}]
        }
    )

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

    except ClientError:
        return "Invalid API request or configuration."

    except ServerError:
        return "Gemini servers are busy. Please try again later."

    except Exception as e:
        return f"Unexpected Error: {e}"


def clear_chat():
    """Clear conversation history."""
    global chat_history
    chat_history = []