"""doc string placeholder"""

import pygame
from pygame.locals import *

class Paddle(pygame.sprite.Sprite):
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

        pygame.draw.rect(self.image, self.color, [0,0,self.width,self.height])

        self.rect = self.image.get_rect()

    # def moveX(self):
    #     How to set mousemotion event in a class object?