import numpy as np
from collections import defaultdict

class MonteCarloAgent:
    def __init__(self):
        self.action_space = [-1, 0, 1]
        # might needs to be replaced with random values for Q that sum to one
        self.Q = defaultdict(lambda: np.zeros(len(self.action_space)))
        self.N = defaultdict(lambda: np.zeros(len(self.action_space)))
        self.epsilon = 1.0
        self.gamma = 0.9  # discount factor

    def update_Q(self, episode, total_reward):
        for s, a, r in reversed(episode):
            # print(s, a, r)
            sa = (tuple(s[0]), tuple(s[1]), tuple(s[2]),tuple(s[3]), tuple(tuple(tuple(brick) for brick in bricks) for bricks in s[4]), a)
            self.N[sa] += 1
            self.Q[sa] += (total_reward - self.Q[sa]) / self.N[sa]
            total_reward *= self.gamma


    def act(self, state, train=True):
        state_tuple = (tuple(state[0]), tuple(state[1]), tuple(state[2]), state[3],tuple(tuple(tuple(brick) for brick in bricks) for bricks in state[4]))
        if train and np.random.rand() <= self.epsilon:
            return np.random.choice(self.action_space)
        else:
            # make sure that a random action is taken that has the max value
            # randomly (argmax alone takes allways the first option)
            q_values = [self.Q[(state_tuple, action)] for action in self.action_space]
            print(self.action_space[np.argmax[q_values]])
            return self.action_space[np.argmax(q_values)]

    def update_epsilon(self, t):
        self.epsilon = max(1.0 / (1.0 + t), 0.05)

# function return function (as needed by defaultdict)
# to create array with rand values that  sum to 1
def normalizedProps(size):
    randomArray=np.random.rand(size)
    randomArray/= randomArray.sum()
    return (lambda: randomArray)

