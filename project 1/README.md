markdown
# AI Internship Project 1 - Rule-Based AI Chatbot

## Project Overview

This project is a simple rule-based AI chatbot created using Python.

The chatbot takes input from the user, cleans the input, detects the user's intent, and gives a predefined response. It runs in a continuous loop and stops only when the user types an exit command like `bye`, `exit`, or `quit`.

This project is part of Week 1 of the Artificial Intelligence internship.

## Project Goal

The goal of this project is to understand the basic logic behind chatbots and AI systems.

This chatbot does not use machine learning or deep learning. Instead, it uses predefined rules, conditions, dictionaries, and functions to respond to user messages.

## Features

- Handles greetings
- Handles exit commands
- Runs in a continuous loop
- Cleans user input using lowercase and strip methods
- Detects user intent
- Uses dictionaries for storing responses
- Gives random replies from predefined response lists
- Answers basic questions about:
  - Artificial Intelligence
  - Python
  - Chatbots
  - Rule-based AI
  - Internship project
- Can tell the current date and time
- Can remember the user's name during the current chat session
- Gives fallback response when it does not understand the input

## Technologies Used

- Python
- Control flow
- If-else conditions
- Functions
- Dictionaries
- Loops
- Random module
- Datetime module

## How to Run the Project

1. Install Python on your computer.
2. Create a file named `chatbot.py`.
3. Copy the chatbot code into the file.
4. Open terminal or command prompt.
5. Run the file using this command:

bash
python chatbot.py
`

If your system uses Python 3 separately, run:

bash
python3 chatbot.py
## Example Conversation

text
Nova: Welcome to the AI Internship Chatbot!
Nova: I am a rule-based chatbot created in Python.
Nova: Type 'help' to see what you can ask.
Nova: Type 'bye', 'exit', or 'quit' to stop the chatbot.

You: hello
Nova: Hello! How can I help you today?

You: what is ai
Nova: AI means making computers smart enough to solve problems, answer questions, and make decisions.

You: what is python
Nova: Python is a popular programming language used in AI, web development, automation, and data science.

You: my name is Ahmed
Nova: Nice to meet you, Ahmed!

You: time
Nova: The current time is 08:30 PM.

You: bye
Nova: Goodbye! Best of luck with your AI internship.


## Concepts Learned

Through this project, I learned:

* How to take input from users
* How to clean user input
* How to use a continuous loop
* How to use if-else logic
* How to create reusable functions
* How to use dictionaries for better response management
* How a rule-based chatbot works
* How simple AI systems can be built using decision-making logic