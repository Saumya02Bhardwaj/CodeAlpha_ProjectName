
# Basic Rule-Based Chatbot

def chatbot():
    print("==============================")
    print("       WELCOME TO CHATBOT")
    print("==============================")
    print("Chatbot: Hello! I am your Python chatbot.")
    print("Chatbot: You can say hello, ask how are you, or say bye.")

    while True:
        user_input = input("\nYou: ").lower().strip()

        if user_input == "hello":
            print("Chatbot: Hi!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks! How about you?")

        elif user_input == "what is your name":
            print("Chatbot: I am a simple Python chatbot.")

        elif user_input == "good morning":
            print("Chatbot: Good morning! Have a great day.")

        elif user_input == "thank you":
            print("Chatbot: You're welcome!")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")

# Call the chatbot function
chatbot()
