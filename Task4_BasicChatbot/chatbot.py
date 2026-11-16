
# =====================================
# CodeAlpha Internship - Task 4
# Basic Chatbot
# =====================================

def chatbot_response(user_input):

    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi! Welcome! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks! How are you?"

    elif user_input == "what is your name":
        return "I'm Python Chatbot!"

    elif user_input == "what can you do":
        return "I can chat with you and answer simple questions!"

    elif user_input == "thank you" or user_input == "thanks":
        return "You're welcome! Happy to help."

    elif user_input == "good morning":
        return "Good morning! Have a wonderful day!"

    elif user_input == "good night":
        return "Good night! Sweet dreams!"

    elif user_input == "who created you":
        return "I was created using Python programming!"

    elif user_input == "bye" or user_input == "exit":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that. Try another message."


# Main chatbot program

print("===================================")
print("       WELCOME TO PYTHON CHATBOT")
print("===================================")
print("Type 'bye' or 'exit' to end the chat.")

# Store conversation history
chat_history = []

while True:

    user = input("\nYou: ")

    response = chatbot_response(user)

    print("Bot:", response)

    # Save conversation
    chat_history.append("You: " + user)
    chat_history.append("Bot: " + response)

    if user.lower().strip() == "bye" or user.lower().strip() == "exit":
        break


# Display conversation history
print("\n========== CHAT HISTORY ==========")

for message in chat_history:
    print(message)

print("===================================")
print("Thank you for chatting!")
