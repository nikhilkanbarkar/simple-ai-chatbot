from chatbot import get_ai_response, clear_chat

print("=" * 60)
print("          SIMPLE AI CHAT ASSISTANT")
print("=" * 60)
print("Commands:")
print("  exit  - Close the chatbot")
print("  clear - Clear conversation history")
print("=" * 60)

while True:
    user_input = input("\nYou : ").strip()

    if not user_input:
        print("AI  : Please enter a message.")
        continue

    if user_input.lower() == "exit":
        print("\nAI  : Goodbye! Have a great day! 👋")
        break

    if user_input.lower() == "clear":
        clear_chat()
        print("\nAI  : Conversation history cleared.")
        continue

    reply = get_ai_response(user_input)

    print(f"\nAI  : {reply}")