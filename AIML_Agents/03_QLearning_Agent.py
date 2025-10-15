# 03_QLearning_Agent.py
# ---------------------
# A simple Q-Learning agent that learns to navigate a 1D grid world.
# Goal: Reach the rightmost cell (Reward +10).
# Trap: Avoid the cell before the goal (Reward -10).
# Step cost: -1.

import random

class GridWorld:
    def __init__(self, size=6):
        self.size = size
        self.state = 0 # Start at left
        self.goal = size - 1
        self.trap = size - 2
    
    def reset(self):
        self.state = 0
        return self.state
    
    def step(self, action):
        # Actions: 0 = Left, 1 = Right
        if action == 1: # Right
            self.state = min(self.size - 1, self.state + 1)
        elif action == 0: # Left
            self.state = max(0, self.state - 1)
        
        # Rewards
        if self.state == self.goal:
            return self.state, 10, True # Done
        elif self.state == self.trap:
            return self.state, -10, True # Done (Fell in trap)
        else:
            return self.state, -1, False # Step cost

class QLearningAgent:
    def __init__(self, state_size, action_size, learning_rate=0.1, discount_factor=0.9, epsilon=0.1):
        self.q_table = [[0.0 for _ in range(action_size)] for _ in range(state_size)]
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon
        self.action_size = action_size
    
    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, self.action_size - 1) # Explore
        else:
            # Exploit: choose best action
            return self.q_table[state].index(max(self.q_table[state]))

    def learn(self, state, action, reward, next_state):
        predict = self.q_table[state][action]
        target = reward + self.gamma * max(self.q_table[next_state])
        self.q_table[state][action] += self.lr * (target - predict)

def main():
    env = GridWorld(size=6)
    agent = QLearningAgent(state_size=6, action_size=2)
    
    episodes = 500
    
    print("--- Q-Learning Agent ---")
    print("Training...")
    
    for episode in range(episodes):
        state = env.reset()
        done = False
        
        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.learn(state, action, reward, next_state)
            state = next_state
            
    print("Training complete.")
    print("\nLearned Q-Table:")
    print("State | Left (Q) | Right (Q)")
    for i, row in enumerate(agent.q_table):
        print(f"  {i}   |  {row[0]:.2f}   |  {row[1]:.2f}")
        
    print("\nTesting Policy:")
    state = env.reset()
    path = [state]
    done = False
    while not done:
        # Turn off exploration for testing
        action = agent.q_table[state].index(max(agent.q_table[state]))
        state, _, done = env.step(action)
        path.append(state)
        
    print("Path taken:", path)
    if path[-1] == env.goal:
        print("Agent reached the goal!")
    else:
        print("Agent failed.")

if __name__ == "__main__":
    main()

# Updated agent logic on 2025-10-15
