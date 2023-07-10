import numpy as np
from Breakout_Class_Test import Breakout
from Agents.Q_Deep_Agent import MonteCarloAgent

# Initialize the environment and the agent
env = Breakout()
state_size = len(env._get_state())  # You might want to adjust this depending on how you represent states
action_size = 3  # 3 possible actions
agent = MonteCarloAgent(state_size, action_size)

# Number of episodes to run the simulation
episodes = 1000

for e in range(episodes):
    # Reset state at the beginning of each game
    state = env.reset()
    state = np.reshape(state, [1, state_size])

    done = False
    while not done:
        # Agent takes action
        action = agent.act(state)
        
        # Retrieve the next state, reward, and whether the episode is done
        next_state, reward, done = env.step(action)
        next_state = np.reshape(next_state, [1, state_size])
        
        # Remember the previous state, action, reward, and done
        agent.remember(state, action, reward, next_state, done)
        
        # Make next_state the new current state for the next frame.
        state = next_state
        
        # done becomes True when the game ends
        if done:
            # Print result every episode
            print("episode: {}/{}, score: {}"
                  .format(e, episodes, reward))

            # Replay and learn from the past experiences
            agent.replay()
