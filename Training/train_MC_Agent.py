import numpy as np
import matplotlib.pyplot as plt

import visualizer as visualizer

def train_agent(agent, env, episodes, render=False, exploring_starts=True):
    rewards = []
    timestep = 0
    rewards_per_timestep = []

    for episode in range(episodes):
        # Reset environment and get initial state
        #state = env.reset()

        # Exploring starts random start state
        if (exploring_starts):
            state = env.random_reset()
        else:
            state = env.ingame_reset()

        done = False
        # exploring start random first action

        # Record the transitions
        transitions = []
        total_reward = 0

        # random action in timestep 0
        action = np.random.choice(agent.action_space)
        next_state, reward, done = env.step(action)
        # Record the transition
        transitions.append((state, action, reward))

        total_reward += reward
        state = next_state

        while not done:
            # Choose action based on the agent's policy
            action = agent.act(state)
            
            env.render()

            # Execute the action in the environment
            next_state, reward, done = env.step(action)
            # Record the transition

            # have to take the bricks list and make it an immutable item

            transitions.append((state, action, reward))
            total_reward += reward
            state = next_state

            rewards_per_timestep.append([timestep, total_reward, episode]) # for plotting 
            timestep += 1 
            

        # After each episode, update the agent's Q values
        agent.update_Q(transitions, total_reward)

        # Store the reward
        rewards.append(total_reward)

        # Reduce the epsilon (Exploration vs. Exploitation trade-off)
        agent.update_epsilon(episode)

        if (episode+1) % 100 == 0:
            print(f'Episode {episode+1}/{episodes}: Reward {total_reward}')

        if (episode+1)== episodes:
            print("done")

    visualizer.rewards_time(rewards_per_timestep)


    return rewards


def plot_rewards(rewards, moving_avg_window=10):
    # Plot raw rewards
    plt.plot(rewards, label='Raw rewards')

    # Also plot the moving average of rewards
    moving_avg_rewards = np.convolve(rewards, np.ones(moving_avg_window)/moving_avg_window, mode='valid')
    plt.plot(range(moving_avg_window-1, len(rewards)), moving_avg_rewards, label=f'Moving average ({moving_avg_window} episodes)')

    # Add labels and legend
    plt.title('Rewards per episode')
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.legend()

    # Set y-axis limit
    plt.ylim([-1000, plt.ylim()[1]])

    plt.show()