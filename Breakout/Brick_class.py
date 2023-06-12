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


class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)