import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define game constants, multiplied by 20 for visuals
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BALL_RADIUS = 20
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
BRICK_WIDTH = 60
BRICK_HEIGHT = 20

class renderer:
    def __init__(self, env):
        self.env = env
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Breakout")

    def draw(self, ball_position, paddle_position, bricks):
        self.screen.fill(BLACK)

        # Draw bricks
        for brick in bricks:
            pygame.draw.rect(self.screen, WHITE, (brick[0][0], brick[0][1], BRICK_WIDTH, BRICK_HEIGHT))

        # Draw paddle
        pygame.draw.rect(self.screen, WHITE, (paddle_position[0], paddle_position[1], PADDLE_WIDTH, PADDLE_HEIGHT))

        # Draw ball
        pygame.draw.circle(self.screen, WHITE, (ball_position[0], ball_position[1]), BALL_RADIUS)

        pygame.display.flip()

    def render(self):
        state = self.env._get_state()
        ball_position = state[0]
        paddle_position = state[2]
        bricks = state[4]
        self.draw(ball_position, paddle_position, bricks)