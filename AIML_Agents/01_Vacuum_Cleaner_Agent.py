# 01_Vacuum_Cleaner_Agent.py
# --------------------------
# A Simple Reflex Agent for the Vacuum Cleaner World.
# The agent perceives its location (A or B) and the status (Dirty or Clean).
# Rules:
# 1. If status is Dirty -> Suck
# 2. If status is Clean and location is A -> Move Right
# 3. If status is Clean and location is B -> Move Left

import random

class Environment:
    def __init__(self):
        # Initial state: Randomly dirty or clean
        self.locationCondition = {'A': random.choice(['Clean', 'Dirty']), 
                                  'B': random.choice(['Clean', 'Dirty'])}
        # Agent starts at random location
        self.agentLocation = random.choice(['A', 'B'])

class SimpleReflexAgent:
    def __init__(self, env):
        self.env = env
        self.performance = 0

    def perceive(self):
        return self.env.agentLocation, self.env.locationCondition[self.env.agentLocation]

    def act(self):
        location, status = self.perceive()
        print(f"Agent at {location}. Status: {status}")

        if status == 'Dirty':
            return 'Suck'
        elif location == 'A':
            return 'Right'
        elif location == 'B':
            return 'Left'
    
    def run(self, steps=5):
        print("--- Vacuum Cleaner Agent Started ---")
        print(f"Initial State: {self.env.locationCondition}")
        
        for _ in range(steps):
            action = self.act()
            print(f"Action: {action}")
            
            if action == 'Suck':
                self.env.locationCondition[self.env.agentLocation] = 'Clean'
                self.performance += 1
                print("Location cleaned.")
            elif action == 'Right':
                self.env.agentLocation = 'B'
                print("Moved to B.")
            elif action == 'Left':
                self.env.agentLocation = 'A'
                print("Moved to A.")
            
            print(f"Current Environment: {self.env.locationCondition}")
            print("-" * 20)
            
            # Check if all clean
            if all(status == 'Clean' for status in self.env.locationCondition.values()):
                print("All locations are clean!")
                break

if __name__ == "__main__":
    env = Environment()
    agent = SimpleReflexAgent(env)
    agent.run()

# Updated agent logic on 2025-10-17
