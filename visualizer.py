import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

imgpath = "./img/"
sns.set_style("whitegrid")


def rewards_time(rewards_per_timestep):
    data = pd.DataFrame(rewards_per_timestep, columns=['step', 'reward'])
    sns.scatterplot(x='step', y='reward', data=data, alpha=0.6)
    plt.savefig(imgpath + 'rewards_time.png', dpi=300)