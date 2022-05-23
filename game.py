"""My version of the classic Breakout game"""

from Paddle import Paddle
import pygame
from pygame.locals import *

pygame.init()

SIZE = 900, 1100
SCREEN_WIDTH, SCREEN_HEIGHT = SIZE
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Breakthrough')


paddle_width = 180
paddle_height = 20
paddle = Paddle(width=paddle_width, height=paddle_height, color=Color('red'))
paddle.rect.x = SCREEN_WIDTH/2
paddle.rect.y = SCREEN_HEIGHT-70

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddle)


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        # Paddle Movement
        elif event.type == MOUSEMOTION:
            paddle.rect.x = event.pos[0] - (paddle_width/2)
            if paddle.rect.x <= 0:
                paddle.rect.x = 0
            elif paddle.rect.x >= SCREEN_WIDTH - paddle_width:
                paddle.rect.x = SCREEN_WIDTH - paddle_width


    all_sprites_list.update()

    screen.fill('gray')
    all_sprites_list.draw(screen)
    pygame.display.update()

    clock.tick(60)

pygame.quit()