import itertools
import matplotlib.pyplot as plt
import numpy as np
from Breakout_Class_Test import Breakout
from Monte_Carlo_Agent import MonteCarloAgent

# Initialize the game environment and agent
grid_size = (15, 10)
num_bricks = 5
num_episodes = 1000

env = Breakout(grid_size=grid_size, num_bricks=num_bricks)
agent = MonteCarloAgent(num_actions=3, num_states=np.prod(grid_size), epsilon=0.1)

# Monitor the total reward per episode
rewards = []

# Main loop
for episode_num in range(num_episodes):
    state = env.reset()
    episode = []
    total_reward = 0

    # Generate an episode
    for t in itertools.count():
        # Choose an action based on the current state
        action = agent.choose_action(state)

        # Perform the action and get the new state and reward
        next_state, reward, done = env.step(action)

        # Store the transition in the episode
        episode.append((state, action, reward))
        
        # Update the total reward
        total_reward += reward

        # Update the current state
        state = next_state

        if done:
            break

    # Learn from the episode
    agent.learn(episode)

    # Store the total reward
    rewards.append(total_reward)

    if episode_num % 100 == 0:
        print(f'Episode {episode_num}/{num_episodes}. Total reward: {total_reward}')

# Plot the total reward per episode
plt.plot(rewards)
plt.xlabel('Episode')
plt.ylabel('Total Reward')
plt.show()
