from config import client, MODEL_NAME


def get_ai_response(prompt):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text