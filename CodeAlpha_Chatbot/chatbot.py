print("🌸 Welcome to ChatBot 🌸")
print("Type 'bye' to exit\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hii bestie ")

    elif user == "hiiie":
        print("Bot: Hello!! What's up? ✨")

    elif user == "hii":
        print("Bot: Hieee! What's for today?! 🌸")

    elif user == "how are you":
        print("Bot: I'm doing amazing today ✨")

    elif user == "your name":
        print("Bot: I'm CodeAlpha Bot 🤖")

    elif user == "favorite color":
        print("Bot: Pink obviously 🎀")
    elif user == "what's your favorite color":
        print("Bot: Black wby?")

    elif user == "bye":
        print("Bot: Goodbye! Take care 💖")
        break

    else:
        print("Bot: Hmm... I don't understand that 😭")