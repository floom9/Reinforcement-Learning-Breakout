import pygame
from pygame.locals import *
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define game constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BALL_RADIUS = 10
PADDLE_WIDTH = 75
PADDLE_HEIGHT = 15
BRICK_WIDTH = 60
BRICK_HEIGHT = 20


class Paddle:
    def __init__(self):
        self.pos = [(SCREEN_WIDTH - PADDLE_WIDTH) // 2, SCREEN_HEIGHT - PADDLE_HEIGHT * 2]
        self.vel = 0

    def move_left(self):
        self.vel = -5

    def move_right(self):
        self.vel = 5

    def stop(self):
        self.vel = 0

    def update(self):
        self.pos[0] += self.vel
        if self.pos[0] < 0:
            self.pos[0] = 0
        elif self.pos[0] > SCREEN_WIDTH - PADDLE_WIDTH:
            self.pos[0] = SCREEN_WIDTH - PADDLE_WIDTH