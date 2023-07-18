import numpy as np
from Breakout.Breakout_Class import Breakout
from Agents.Monte_Carlo_Agent import MonteCarloAgent_Explorer
from Training.train_MC_Agent import train_agent, plot_rewards
import pickle


env = Breakout(max_timesteps=1000)
agent = MonteCarloAgent_Explorer()

# Let's train the agent for 1000 episodes
rewards = train_agent(agent, env, 1000,exploring_starts=False)

plot_rewards(rewards)

#with open('Agents/agent.pkl', 'wb') as f:
#    pickle.dump(agent, f)