from chatbot import get_ai_response, clear_chat

print("=" * 50)
print("Simple AI Chat Assistant")
print("Type 'exit' to quit")
print("Type 'clear' to clear chat history")
print("=" * 50)

while True:
    user_input = input("\nYou : ").strip()

    if user_input.lower() == "exit":
        print("AI : Goodbye! 👋")
        break

    if not user_input:
        print("AI : Please enter a message.")
        continue

    if user_input.lower() == "clear":
        clear_chat()
        print("AI : Conversation history cleared.")
        continue

    reply = get_ai_response(user_input)
    print(f"AI : {reply}")