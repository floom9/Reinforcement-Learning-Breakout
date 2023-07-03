from Breakout_Class_Test import Breakout

game = Breakout()
print(game.reset()) # Should print the initial state

for _ in range(100):
    state, reward, done = game.step(1) # Try moving the paddle to the right
    print(reward, done) 
