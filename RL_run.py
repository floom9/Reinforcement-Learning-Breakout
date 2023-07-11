import numpy as np
from Breakout.Breakout_Class import Breakout
from Agents.Monte_Carlo_Agent import MonteCarloAgent
from Training.train_MC_Agent import train_agent

env = Breakout()
agent = MonteCarloAgent()

# Let's train the agent for 1000 episodes
rewards = train_agent(agent, env, 10000)

