from Game_classes import Ball, Paddle, Brick, BreakoutGame
import pygame
from pygame.locals import *


# Initialize Pygame
pygame.init()

# Create game objects
ball = Ball(BALL_RADIUS)
paddle = Paddle(PADDLE_WIDTH, PADDLE_HEIGHT)
bricks = [Brick(2, 2), Brick(8, 2), Brick(14, 2)]
game = BreakoutGame(SCREEN_WIDTH, SCREEN_HEIGHT)

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
    if ball.pos[0] < ball.radius or ball.pos[0] > game.SCREEN_WIDTH - ball.radius:
        ball.reverse_velocity_x()
    if ball.pos[1] < ball.radius:
        ball.reverse_velocity_y()

    if ball.pos[1] > game.SCREEN_HEIGHT - ball.radius - paddle.height and paddle.pos[0] <= ball.pos[0] <= paddle.pos[0] + paddle.width:
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

    pygame.draw.rect(game.screen, game.WHITE, (paddle.pos[0], paddle.pos[1], paddle.width, paddle.height))
    pygame.draw.circle(game.screen, game.WHITE, (ball.pos[0], ball.pos[1]), ball.radius)

    pygame.display.flip()
    game.clock.tick(60)

# Quit Pygame
pygame.quit()
