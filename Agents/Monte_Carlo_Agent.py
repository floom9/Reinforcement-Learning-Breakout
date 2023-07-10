import numpy as np
from collections import defaultdict

class MonteCarloControlAgent:
    def __init__(self, action_space):
        self.action_space = action_space
        self.Q = defaultdict(lambda: np.zeros(action_space.n))
        self.N = defaultdict(lambda: np.zeros(action_space.n))
        self.epsilon = 1.0
        self.gamma = 0.9  # discount factor

    def update_Q(self, episode, total_reward):
        visited_state_actions = set()  # Used for first-visit MC
        for s, a, r in reversed(episode):
            sa = (s, a)
            if sa not in visited_state_actions:
                self.N[sa] += 1
                self.Q[sa] += (total_reward - self.Q[sa]) / self.N[sa]
                visited_state_actions.add(sa)
            total_reward *= self.gamma

    def act(self, state, train=True):
        if train and np.random.rand() <= self.epsilon:
            return np.random.choice(self.action_space)
        else:
            return np.argmax(self.Q[state])

    def update_epsilon(self, t):
        self.epsilon = max(1.0 / (1.0 + t), 0.05)