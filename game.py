"""My version of the classic Breakout game"""

from Paddle import Paddle
from Brick import Brick
from Ball import Ball
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

ball_width, ball_height = 20, 20
ball = Ball(ball_width, ball_height, Color('blue'))
ball.rect.x = 0
ball.rect.y = SCREEN_HEIGHT-100

brick_width, brick_height = 100, 50
brick1 = Brick(100, 50, Color('green'))
brick1.rect.x = 100
brick1.rect.y = SCREEN_HEIGHT/10

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddle)
all_sprites_list.add(brick1)
all_sprites_list.add(ball)

ball_motion = [3,-3]


running = True
paused = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            
            # Pause game
            if event.key == K_ESCAPE:
                paused = True
                while paused:
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                running = True
                                paused = False


        # Paddle Movement
        elif event.type == MOUSEMOTION:
            paddle.rect.x = event.pos[0] - (paddle_width/2)
            if paddle.rect.x <= 0:
                paddle.rect.x = 0
            elif paddle.rect.x >= SCREEN_WIDTH - paddle_width:
                paddle.rect.x = SCREEN_WIDTH - paddle_width

    # Ball movement
    if ball.rect.right > SCREEN_WIDTH:
        ball_motion[0] *= -1
    elif ball.rect.left < 0:
        ball_motion[0] *= -1
    elif ball.rect.top < 0:
        ball_motion[1] *= -1
    # elif ball.rect.bottom > SCREEN_HEIGHT - 70:
    #     ball_motion[1] *= -1

    ball.rect.move_ip(ball_motion)

    all_sprites_list.update()

    screen.fill('gray')
    all_sprites_list.draw(screen)
    pygame.display.update()

    clock.tick(60)

pygame.quit()