import numpy as np
from Breakout.Breakout_Class import Breakout
from Agents.Monte_Carlo_Agent import MonteCarloAgent_ES, MonteCarloAgent_FV
from Testing.testing_MC_Agent import test_agent_average_Reward, test_agent_certain_start
import time
import pickle
import json


method="ES"
#method="FV"
maxTimesteps= 100000
numOfEpisodes= 1000
#brick_layout="TopRow"
#brick_layout="MiddleRow"
brick_layout="ReversePyramid"
num_bricks=9


CalculateAvgReward= True



TrainInfoFilePath=brick_layout+ '_NumBricks_' + str(num_bricks) + 'Method_' + method + '_Episodes_' + str(numOfEpisodes) + '_maxTimesteps_' + str(maxTimesteps)

AgentPath = 'TrainedAgents/' +TrainInfoFilePath +'.pkl'
print("retriving Agent")
with open(AgentPath, 'rb') as f:
    agent = pickle.load(f)
print("retriving Agent done")

if CalculateAvgReward:
    env = Breakout(max_timesteps=maxTimesteps, brick_layout=brick_layout, num_bricks=num_bricks)
    startTime= time.time()
    # Let's train the agent for 1000 episodes
    rewards, exectuionTimes = test_agent_average_Reward(agent=agent, env=env, episodes=numOfEpisodes)
    endTime= time.time()

    avgReward = sum(rewards)/len(rewards)
    print('Average Reward:{}'.format(avgReward))

    overallTestTime = endTime-startTime
    avgExecutionTime = sum(exectuionTimes)/len(exectuionTimes)

    jsonPath= 'CompTimesAndAvgRewards/' +TrainInfoFilePath +'.json'
    with open(jsonPath, "r") as openfile:
        keyFindingsDict = json.load(openfile)

        
    keyFindingsDict['AvgTestingReward']=avgReward
    keyFindingsDict['AvgTestingTimePerEps']= avgExecutionTime


    with open(jsonPath, 'w') as outfile:
        json.dump(keyFindingsDict, outfile)
        




env2 = Breakout(max_timesteps=maxTimesteps, rendering=True, brick_layout=brick_layout, num_bricks=num_bricks)
#create visulsation for the given starting direction of ball -2,-1,0,1,2
transitions=test_agent_certain_start(agent=agent, env=env2, render=True, startingDirection= 2)

