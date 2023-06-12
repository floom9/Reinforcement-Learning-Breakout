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


class Ball:
    def __init__(self):
        self.pos = [random.randint(BALL_RADIUS, SCREEN_WIDTH - BALL_RADIUS), SCREEN_HEIGHT // 2]
        self.vel = [random.randint(2, 4), random.randint(2, 4)]

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def reverse_velocity_x(self):
        self.vel[0] = -self.vel[0]

    def reverse_velocity_y(self):
        self.vel[1] = -self.vel[1]