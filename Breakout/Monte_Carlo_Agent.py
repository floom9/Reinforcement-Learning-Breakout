import numpy as np

class MonteCarloAgent:
    def __init__(self, num_actions, num_states, discount_factor=1.0, epsilon=0.1):
        self.num_actions = num_actions
        self.num_states = num_states
        self.epsilon = epsilon
        self.discount_factor = discount_factor

        # Initialize Q-table with zeros
        self.Q = np.zeros((num_states, num_actions))
        self.returns_sum = np.zeros((num_states, num_actions))
        self.returns_count = np.zeros((num_states, num_actions))

    def choose_action(self, state):
        # Implement epsilon-greedy policy
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.num_actions)  # exploration
        else:
            return np.argmax(self.Q[state])  # exploitation

    def learn(self, episode):
        """ Update the action-value function using the episode's returns """
        states, actions, rewards = zip(*episode)

        # Compute the discounts
        discounts = np.array([self.discount_factor**i for i in range(len(rewards)+1)])

        # Update the Q-table
        for i, state in enumerate(states):
            # Calculate the return
            G = sum(rewards[i:]*discounts[:-(i+1)])
            self.returns_sum[state][actions[i]] += G
            self.returns_count[state][actions[i]] += 1.0
            self.Q[state][actions[i]] = self.returns_sum[state][actions[i]] / self.returns_count[state][actions[i]]
