# Reinforcement-Learning-Breakout
Applying Reinforcement Learning for the videogame Breakout (1976)

## Setup
Environment:

```bash 
conda create -n breakout python=3.10
conda activate breakout
pip install -r requirements.txt
```

Ran into some issues using pygame for rendering. Installing it from the conda-forge repository works: 

```bash
conda install -c conda-forge pygame
```