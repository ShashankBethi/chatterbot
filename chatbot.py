import nltk
from nltk.chat.util import Chat, reflections

nltk.download("punkt")  # Download NLTK data

# Define pairs of patterns and responses
pairs = [
    ["(hello|hi|hey)", ["Hello!", "Hi there!", "Hey!"]],
    ["(how are you|how's it going)", ["I'm just a chatbot.", "I'm doing fine, thank you."]],
    ["(what's your name|who are you)", ["I'm a simple chatbot.", "I'm ChatBot, nice to meet you!"]],
    ["(bye|goodbye)", ["Goodbye!", "Have a great day!", "See you later!"]],
    ["default", ["I'm not sure how to respond to that."]],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def main():
    print("ChatBot: Hi there! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()
