"""doc string placeholder"""

import pygame
from pygame.locals import *

class Ball(pygame.sprite.Sprite):
    """doc string placeholder"""

    def __init__(self, width, height, color):
        """doc string placeholder"""
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(Color('white'))
        self.image.set_colorkey(Color('white'))

        self.width = width
        self.height = height
        self.color = color

        pygame.draw.rect(self.image, color, [0,0,width,height])
        self.rect = self.image.get_rect()