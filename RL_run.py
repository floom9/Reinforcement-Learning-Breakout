import numpy as np
from Breakout.Breakout_Class import Breakout
from Agents.Monte_Carlo_Agent import MonteCarloAgent_ES, MonteCarloAgent_FV
from Training.train_MC_Agent import train_agent, plot_rewards
import time
import pickle

shouldRender= False
#method="ES"
method="FV"
maxTimesteps= 100000
numOfEpisodes= 1000
saveAgent= True
plotRewards= True




if method== "ES":
    agent = MonteCarloAgent_ES()
    exploringStarts=True
elif method == "FV":
    agent = MonteCarloAgent_FV()
    exploringStarts = False
else: 
    raise TypeError("Method must be either ES or FV but is {}".format(method))

env = Breakout(max_timesteps=maxTimesteps, rendering=shouldRender)
startTime= time.time()
# Let's train the agent for 1000 episodes
rewards, exectuionTimes = train_agent(agent=agent, env=env, episodes=numOfEpisodes, exploring_starts=exploringStarts,render=shouldRender)
endTime= time.time()

overallTrainingTime = endTime-startTime
avgExecutionTime = sum(exectuionTimes)/len(exectuionTimes)


keyFindingsDict= {'Overall Training Time': overallTrainingTime,
                  'avgExcutionTime' :  avgExecutionTime,
}


TrainInfoFilePath= 'Method_' + method + '_Episodes_' + str(numOfEpisodes) + '_maxTimesteps_' + str(maxTimesteps) +'_Render_' + str(shouldRender)


if plotRewards:
    print("Plotting Rewards")
    print("close plot to proceed")
    plot_rewards(rewards, moving_avg_window=10, savePath=TrainInfoFilePath)
    print("Ploting Rewards done")


if saveAgent:
    print("saving Agent")
    AgentPath = 'TrainedAgents/' +TrainInfoFilePath +'.pkl'
    with open(AgentPath, 'wb') as f:
        pickle.dump(agent, f)
    print("saving Agent done")

print("done")