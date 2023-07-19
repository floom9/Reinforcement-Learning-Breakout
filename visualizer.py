import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os 

imgpath = "./img/"
sns.set_style("whitegrid")


def rewards_time(rewards_per_timestep):
    data = pd.DataFrame(rewards_per_timestep, columns=['step', 'reward', 'episode'])
    sns.scatterplot(x='step', y='reward', data=data, hue='episode', alpha=0.6)
    plt.savefig(imgpath + 'rewards_time.png', dpi=300)


def saveGIF(name): 
    # Using external library ImageMagick for automatic gif creation
    os.system(f'magick convert -size 600x400 -delay 10 -loop 0 ./.tmp/*.png img/{name}.gif')
    # remove files
    for filename in os.listdir('.tmp'):   
        os.unlink(f'.tmp/{filename}')