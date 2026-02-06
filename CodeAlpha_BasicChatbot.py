# Basic Chatbot

print("Chatbot: Hello! I am a ChatBot. Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user in ["hello", "hi", "hey"]:
        print("Chatbot: Hi there!")

    elif user in ["how are you", "how are you?"]:
        print("Chatbot: I am fine, thanks!")

    elif user == "bye":
        print("Chatbot: Goodbye!")
        break

    else:
        print("Chatbot: Sorry, I don't understand.")
