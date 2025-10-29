# 04_Chatbot_Agent.py
# -------------------
# A simple rule-based chatbot using Regular Expressions.

import re
import random

class ChatbotAgent:
    def __init__(self):
        self.rules = {
            r'hello|hi|hey': ['Hello!', 'Hi there!', 'Greetings!'],
            r'how are you': ['I am doing well, thank you!', 'I am just a computer program, but I feel great!'],
            r'what is your name': ['I am a Python Chatbot.', 'You can call me PyBot.'],
            r'bye|goodbye': ['Goodbye!', 'See you later!', 'Have a nice day!'],
            r'weather': ['I cannot check the weather, but I hope it is sunny!', 'Look out the window!'],
            r'help': ['I can answer simple questions. Try asking my name or how I am.']
        }
        self.default_responses = ["I'm not sure I understand.", "Could you repeat that?", "Interesting."]

    def get_response(self, user_input):
        user_input = user_input.lower()
        
        for pattern, responses in self.rules.items():
            if re.search(pattern, user_input):
                return random.choice(responses)
        
        return random.choice(self.default_responses)

    def chat(self):
        print("--- Chatbot Agent ---")
        print("Type 'bye' to exit.")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['bye', 'goodbye', 'exit', 'quit']:
                print("Bot: Goodbye!")
                break
            
            response = self.get_response(user_input)
            print(f"Bot: {response}")

if __name__ == "__main__":
    bot = ChatbotAgent()
    
    # For automation, we will simulate a conversation instead of using input() loop if running non-interactively
    # But I will leave the interactive loop in the 'chat' method and call a simulation here.
    
    print("--- Simulating Conversation ---")
    test_inputs = ["Hello", "What is your name?", "How are you?", "What is the weather?", "fsdfsd", "Bye"]
    
    for inp in test_inputs:
        print(f"You: {inp}")
        if inp.lower() in ['bye', 'goodbye']:
             print("Bot: Goodbye!")
             break
        print(f"Bot: {bot.get_response(inp)}")
    
    # Uncomment to run interactively
    # bot.chat()

# Updated agent logic on 2025-10-29
