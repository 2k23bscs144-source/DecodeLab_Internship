import random
import datetime


# ==========================
# AI Internship Rule-Based Chatbot
# Project 1 - DecodeLabs
# ==========================


bot_name = "Nova"


responses = {
    "greetings": [
        "Hello! How can I help you today?",
        "Hi there! Nice to meet you.",
        "Hey! I am ready to chat with you.",
        "Welcome! Ask me anything about AI, Python, or this internship."
    ],

    "how_are_you": [
        "I am doing great. Thanks for asking!",
        "I am just a program, but I am working perfectly!",
        "I am fine and ready to help you."
    ],

    "ai": [
        "Artificial Intelligence is a field of computer science where machines are designed to perform tasks that normally require human intelligence.",
        "AI means making computers smart enough to solve problems, answer questions, and make decisions.",
        "AI helps machines understand data, recognize patterns, and perform intelligent tasks."
    ],

    "python": [
        "Python is a popular programming language used in AI, web development, automation, and data science.",
        "Python is beginner-friendly and widely used for Artificial Intelligence projects.",
        "Python is powerful because it has many useful libraries for AI and machine learning."
    ],

    "chatbot": [
        "A chatbot is a computer program that talks with users and gives replies based on rules or AI models.",
        "A chatbot can answer questions, guide users, and automate simple conversations.",
        "This chatbot is rule-based, which means it replies using predefined rules."
    ],

    "rule_based": [
        "A rule-based chatbot works using fixed rules. It checks the user's message and gives a predefined response.",
        "Rule-based AI does not learn by itself. It follows instructions written by the programmer.",
        "In this project, the chatbot uses conditions and dictionaries to decide what response to give."
    ],

    "internship": [
        "Your Week 1 internship project is to build a rule-based AI chatbot using Python.",
        "This project helps you understand input handling, loops, conditions, and basic AI logic.",
        "Completing this project will help you unlock the next internship tasks."
    ],

    "help": [
        "You can ask me about AI, Python, chatbots, rule-based systems, date, time, or this internship project.",
        "Try asking: what is AI, what is Python, what is chatbot, what is rule-based AI, or type bye to exit."
    ],

    "thanks": [
        "You are welcome!",
        "No problem! Happy to help.",
        "Glad I could help you."
    ],

    "unknown": [
        "Sorry, I do not understand that yet.",
        "I am still learning. Please ask something else.",
        "I don't have a rule for that question right now.",
        "Can you ask that in a simpler way?"
    ],

    "bye": [
        "Goodbye! Have a great day.",
        "Bye! Keep learning and practicing.",
        "Goodbye! Best of luck with your AI internship."
    ]
}


user_name = ""


def clean_input(user_input):
    """
    This function cleans the user's input.
    It converts text to lowercase and removes extra spaces.
    """
    return user_input.lower().strip()


def get_random_response(category):
    """
    This function returns a random response from a selected category.
    """
    return random.choice(responses[category])


def detect_intent(user_input):
    """
    This function checks the user's message
    and decides what the user wants.
    """

    greetings = ["hello", "hi", "hey", "salam", "assalamualaikum"]
    exit_words = ["bye", "exit", "quit", "goodbye"]
    thanks_words = ["thanks", "thank you", "shukriya"]

    if user_input in greetings:
        return "greetings"

    elif user_input in exit_words:
        return "bye"

    elif user_input in thanks_words:
        return "thanks"

    elif "how are you" in user_input:
        return "how_are_you"

    elif "what is ai" in user_input or "artificial intelligence" in user_input:
        return "ai"

    elif "python" in user_input:
        return "python"

    elif "chatbot" in user_input:
        return "chatbot"

    elif "rule based" in user_input or "rule-based" in user_input:
        return "rule_based"

    elif "internship" in user_input or "project" in user_input:
        return "internship"

    elif "help" in user_input:
        return "help"

    elif "time" in user_input:
        return "time"

    elif "date" in user_input:
        return "date"

    elif "your name" in user_input or "who are you" in user_input:
        return "bot_name"

    elif "my name is" in user_input:
        return "user_name"

    else:
        return "unknown"


def generate_response(intent, user_input):
    """
    This function generates the final chatbot response.
    """

    global user_name

    if intent == "time":
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    elif intent == "date":
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        return f"Today's date is {current_date}."

    elif intent == "bot_name":
        return f"My name is {bot_name}. I am your rule-based AI chatbot."

    elif intent == "user_name":
        user_name = user_input.replace("my name is", "").strip().title()

        if user_name:
            return f"Nice to meet you, {user_name}!"
        else:
            return "Please tell me your name like this: My name is Ali."

    elif intent == "unknown":
        return get_random_response("unknown")

    else:
        return get_random_response(intent)


def start_chatbot():
    """
    This function starts the chatbot.
    It keeps running until the user types an exit command.
    """

    print("=" * 50)
    print(f"{bot_name}: Welcome to the AI Internship Chatbot!")
    print(f"{bot_name}: I am a rule-based chatbot created in Python.")
    print(f"{bot_name}: Type 'help' to see what you can ask.")
    print(f"{bot_name}: Type 'bye', 'exit', or 'quit' to stop the chatbot.")
    print("=" * 50)

    while True:
        user_input = input("You: ")
        cleaned_input = clean_input(user_input)

        if cleaned_input == "":
            print(f"{bot_name}: Please type something.")
            continue

        intent = detect_intent(cleaned_input)
        response = generate_response(intent, cleaned_input)

        print(f"{bot_name}: {response}")

        if intent == "bye":
            break


start_chatbot()
 