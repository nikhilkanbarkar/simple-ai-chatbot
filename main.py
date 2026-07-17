from chatbot import get_ai_response

print("=" * 50)
print("Simple AI Chat Assistant")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user_input = input("\nYou : ")

    if user_input.lower() == "exit":
        print("AI : Goodbye!")
        break

    if not user_input.strip():
        print("AI : Please enter a message.")
        continue

    reply = get_ai_response(user_input)

    print(f"AI : {reply}")