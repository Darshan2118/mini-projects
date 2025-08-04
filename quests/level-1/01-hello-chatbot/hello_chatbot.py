# quests/level-1/01-hello-chatbot/hello_chatbot.py

print("🤖 Chatbot: Hi Soul! I'm your mini assistant.")
print("💬 Type 'exit' to end our chat.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "hello":
        print("🤖 Chatbot: Hey there!")
    elif user_input == "bye":
        print("🤖 Chatbot: Catch you later!")
    elif user_input == "thanks":
        print("🤖 Chatbot: Anytime, Soul!")
    elif user_input == "exit":
        print("🤖 Chatbot: Peace out. 👋")
        break
    else:
        print("🤖 Chatbot: Hmm... I didn’t get that. Try 'hello', 'bye', or 'thanks'.")
