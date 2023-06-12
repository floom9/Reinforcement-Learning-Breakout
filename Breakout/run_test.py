from Breakout.Game_classes import Game, Ball, Brick, Paddle
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Create game objects
ball = Ball()
paddle = Paddle()
bricks = [Brick(100, 100), Brick(200, 100), Brick(300, 100)]
game = Game()

# Game loop
while not game.game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            game.game_over = True
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                paddle.move_left()
            elif event.key == K_RIGHT:
                paddle.move_right()
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                paddle.stop()

    # Update game state
    paddle.update()
    ball.update()

    # Check for collisions
    if ball.pos[0] < Ball.RADIUS or ball.pos[0] > game.SCREEN_WIDTH - Ball.RADIUS:
        ball.reverse_velocity_x()
    if ball.pos[1] < Ball.RADIUS:
        ball.reverse_velocity_y()

    if ball.pos[1] > game.SCREEN_HEIGHT - Ball.RADIUS - Paddle.HEIGHT and paddle.pos[0] <= ball.pos[0] <= paddle.pos[0] + Paddle.WIDTH:
        ball.reverse_velocity_y()

    for brick in bricks:
        if brick.rect.collidepoint(ball.pos):
            bricks.remove(brick)
            ball.reverse_velocity_y()
            break

    # Draw objects on the screen
    game.screen.fill(game.BLACK)

    for brick in bricks:
        pygame.draw.rect(game.screen, game.WHITE, brick.rect)

    pygame.draw.rect(game.screen, game.WHITE, (paddle.pos[0], paddle.pos[1], Paddle.WIDTH, Paddle.HEIGHT))
    pygame.draw.circle(game.screen, game.WHITE, (ball.pos[0], ball.pos[1]), Ball.RADIUS)

    pygame.display.flip()
    game.clock.tick(60)

# Quit Pygame
pygame.quit()
