import numpy as np
from Breakout.Breakout_Class import Breakout
from Agents.Monte_Carlo_Agent import MonteCarloAgentES
from Training.train_MC_Agent import train_agent
import pickle

env = Breakout(max_timesteps=1000)
agent = MonteCarloAgentES()

# Let's train the agent for 1000 episodes
rewards = train_agent(agent, env, 1000)

with open('Agents/agent.pkl', 'wb') as f:
    pickle.dump(agent, f)