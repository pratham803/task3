import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data
nltk.download('punkt', quiet=True)

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name\??",
        ["I'm a simple chatbot created with NLTK."]
    ],
    [
        r"how are you\??",
        ["I'm just a program, but I'm doing well!"]
    ],
    [
        r"(.*) your name\??",
        ["My name is NLTK Chatbot."]
    ],
    [
        r"(.*) (help|support)",
        ["Sure, I'm here to help. Please tell me your query."]
    ],
    [
        r"(.*) (give intern)",
        ["sure giv intern bro..."]
    ],
    [
        r"quit|exit|bye",
        ["Goodbye! Have a nice day.", "Bye!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Can you rephrase?"]
    ]
]

def chatbot():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("> ").lower()
        if user_input in ["quit", "exit", "bye"]:
            print("Goodbye! Have a nice day.")
            break
        response = chat.respond(user_input)
        print(response)

if __name__ == "__main__":
    chatbot()