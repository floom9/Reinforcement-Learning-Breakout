import numpy as np
from Breakout.Breakout_Class import Breakout
from Agents.Monte_Carlo_Agent import MonteCarloAgent_ES, MonteCarloAgent_FV
from Training.train_MC_Agent import train_agent, plot_rewards
import pickle

shouldRender= False
method="ES"
#method="FV"
maxTimesteps= 1000
numOfEpisodes= 1000
saveAgent= True
plotRewards= True



env = Breakout(max_timesteps=maxTimesteps, rendering=shouldRender)
if method== "ES":
    agent = MonteCarloAgent_ES()
    exploringStarts=True
elif method == "FV":
    agent = MonteCarloAgent_FV()
    exploringStarts = False
else: 
    raise TypeError("Method must be either ES or FV but is {}".format(method))

# Let's train the agent for 1000 episodes
rewards = train_agent(agent=agent, env=env, episodes=numOfEpisodes, exploring_starts=exploringStarts,render=shouldRender)

if plotRewards:
    print("Plotting Rewards")
    print("close plot to proceed")
    plot_rewards(rewards)
    print("Ploting Rewards done")

TrainInfoFilePath= 'Method_' + method + '_Episodes_' + str(numOfEpisodes) + '_maxTimesteps_' + str(maxTimesteps) +'_Render_' + str(shouldRender)

if saveAgent:
    print("saving Agent")
    AgentPath = 'TrainedAgents/' +TrainInfoFilePath +'.pkl'
    with open(AgentPath, 'wb') as f:
        pickle.dump(agent, f)
    print("saving Agent done")

print("done")