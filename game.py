"""My version of the classic Breakout game"""

import pygame
from pygame.locals import *

pygame.init()

SIZE = 900, 1100
SCREEN_WIDTH, SCREEN_HEIGHT = SIZE
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Breakthrough')

paddle_size = 180, 20
paddle = pygame.Rect((SCREEN_WIDTH/2, SCREEN_HEIGHT-70), paddle_size)


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEMOTION:
            paddle.x = event.pos[0] - (paddle_size[0]/2)
            if paddle.x <= 0:
                paddle.x = 0
            elif paddle.x >= SCREEN_WIDTH - paddle_size[0]:
                paddle.x = SCREEN_WIDTH - paddle_size[0]

            # print(paddle.center)


    screen.fill('gray')
    pygame.draw.rect(screen, Color('red'), paddle)
    pygame.display.update()

    clock.tick(60)

pygame.quit()