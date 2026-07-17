from config import client, MODEL_NAME
from google.genai.errors import ClientError, ServerError


def get_ai_response(prompt):
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        return response.text

    except ClientError as e:
        return f"Client Error: {e}"

    except ServerError:
        return "Gemini servers are busy. Please try again later."

    except Exception as e:
        return f"Unexpected Error: {e}"