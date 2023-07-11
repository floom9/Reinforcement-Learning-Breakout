import numpy as np

class Breakout:
    def __init__(self, grid_size=(15, 10), num_bricks=5, max_timesteps=500):
        self.grid_size = grid_size
        self.num_bricks = num_bricks
        self.paddle_size = 5
        self.max_timesteps=max_timesteps
        self.timesteps= 0
        self.reset()

    def reset(self):
        self.paddle_position = [self.grid_size[0] // 2, self.grid_size[1] - 1] # place paddle in the center
        self.ball_position = [self.paddle_position[0] + self.paddle_size // 2, self.paddle_position[1] - 1] # place ball on top of the paddle
        self.ball_direction = [np.random.choice([-2, -1, 0, 1, 2]), -1] # initial direction of the ball
        self.paddle_speed = 0
        self.bricks = self._generate_bricks() 
        self.done = False
        self.timesteps=0
        return self._get_state()

    def ingame_reset(self):
        self.paddle_position = [self.grid_size[0] // 2, self.grid_size[1] - 1] # place paddle in the center
        self.ball_position = [self.paddle_position[0] + self.paddle_size // 2, self.paddle_position[1] - 1] # place ball on top of the paddle
        self.ball_direction = [np.random.choice([-2, -1, 0, 1, 2]), -1] # initial direction of the ball
        self.paddle_speed = 0
        self.bricks = self._generate_bricks() 
        self.done = False
        return self._get_state()

    def _generate_bricks(self):
        bricks = []
        for i in range(0, self.grid_size[0], 3):  # Step size of 3 to make space for each brick
            brick = []
            for j in range(3):  # For each block of the brick
                if i + j < self.grid_size[0]:  # To prevent bricks going out of the grid
                    brick.append([i + j, 0])  # Arrange the blocks of the brick horizontally
            bricks.append(brick)
        return bricks

    def _get_state(self):
        return [self.ball_position, self.ball_direction, self.paddle_position, self.bricks]

    def step(self, action):
        # Initialize reward
        reward = -1

        action = np.clip(action, -1, 1)
    
        # Update paddle speed, ensure the speed is within the range of [-2, 2]
        self.paddle_speed = np.clip(self.paddle_speed + action, -2, 2)
        
        # Update paddle position based on the speed
        self.paddle_position[0] += self.paddle_speed

        # Ensure the paddle stays within the grid
        self.paddle_position[0] = np.clip(self.paddle_position[0], 0, self.grid_size[0]-self.paddle_size)


        # Update ball position if within the boundaries
        if 0 <= self.ball_position[0] + self.ball_direction[0] <= self.grid_size[0]:
            self.ball_position[0] += self.ball_direction[0]
        else:
            self.ball_position[0] += self.ball_direction[0]
            self.ball_direction[0] *= -1 # Ball gets reflected in x-axis

        if 0 <= self.ball_position[1] + self.ball_direction[1] <= self.grid_size[1]:
            self.ball_position[1] += self.ball_direction[1]
        elif self.ball_position[1] + self.ball_direction[1] == 0: # Ball hits the upper boundary
            self.ball_position[1] += self.ball_direction[1]
            self.ball_direction[1] *= -1 # Ball gets reflected in y-axis



        # Check if ball hits brick
        for brick in self.bricks:
            if self.ball_position in brick:
                self.bricks.remove(brick) # Brick disappears
                self.ball_direction[1] *= -1 # Ball gets reflected
                reward += 1 # reward for hitting a brick
                break

        # Check if ball hits paddle
        if self.paddle_position[0] <= self.ball_position[0] < (self.paddle_position[0] + self.paddle_size) and self.ball_position[1] == self.paddle_position[1]:
            self.ball_direction[1] *= -1

            # Determine the part of the paddle the ball hit
            paddle_part = (self.ball_position[0] - self.paddle_position[0]) // (self.paddle_size // 5)
            paddle_parts = [-2, -1, 0, 1, 2]
            
            # Change horizontal direction based on where the ball hits the paddle
            self.ball_direction[0] = paddle_parts[paddle_part]


        # Check if ball goes past the paddle
        if self.ball_position[1] > self.paddle_position[1]:
            reward += -10 # punishment for missing the ball
            self.ingame_reset()
        # Check if all bricks are destroyed
        if len(self.bricks) == 0:
            self.done = True # End of episode
            reward += 100 # reward for winning the game

        # count timesteps in this run
        self.timesteps +=1
        if self.timesteps >= self.max_timesteps: 
            self.done=True


        return self._get_state(), reward, self.done
