"""My version of the classic Breakout game"""

from Paddle import Paddle
from Brick import Brick
from Ball import Ball
import pygame
from pygame.locals import *
import random

pygame.init()

bkg_img = pygame.image.load('bkg_test.png')
# bkg_img.convert()
bkg_rect = bkg_img.get_rect()

SIZE = 900, 1100
SCREEN_WIDTH, SCREEN_HEIGHT = SIZE
# screen = pygame.display.set_mode(SIZE)
screen = pygame.display.set_mode(bkg_rect.size)
pygame.display.set_caption('Breakthrough')


paddle_width = 150
paddle_height = 20
paddle = Paddle(width=paddle_width, height=paddle_height, color=Color('red'))
paddle.rect.x = SCREEN_WIDTH/2
paddle.rect.y = SCREEN_HEIGHT-70

ball_width, ball_height = 20, 20
ball = Ball(ball_width, ball_height, img='ball.png')
ball.rect.x = 0
ball.rect.y = SCREEN_HEIGHT-100
ball_motion = [7,-7]

# Bricks
brick_width, brick_height = 100, 30
columns = 8
gap_horiz = 0
gap_vertical = 0
rows = 4
gap_brick_sum = gap_horiz + brick_width
x_coord_start = 50
x_coord_counter = x_coord_start
y_coord_current = SCREEN_HEIGHT/5
brick_rows = list()
# Construct Brick Rows
for row in range(1, rows+1):
    b_row = list()
    for column in range(columns):
        b_row.append(Brick(brick_width, brick_height, Color('green')))
    for brick in b_row:
        brick.rect.x = x_coord_counter
        brick.rect.y = y_coord_current + brick_height + gap_vertical
        x_coord_counter += gap_brick_sum
    x_coord_counter = x_coord_start
    y_coord_current += brick_height + gap_vertical
    brick_rows.append(b_row)

# Non-ball sprites list
brick_sprites_list = pygame.sprite.Group()
for row in brick_rows:
    for brick in row:
        brick_sprites_list.add(brick)

# All sprites list
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(ball)
all_sprites_list.add(paddle)
for row in brick_rows:
    for brick in row:
        all_sprites_list.add(brick)

running = True
paused = False
clock = pygame.time.Clock()

collision_buffer = 7

# brick.rect.center coords to store past values to compare and determine ball direction
# start with two fillers so [-2] and [-1] are not out of bounds
brc_x = [0,0]
brc_y = [0,0]

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
            if paddle.rect.left <= 0:
                paddle.rect.left = 0
            elif paddle.rect.right >= SCREEN_WIDTH:
                paddle.rect.right = SCREEN_WIDTH

    # Ball collision
    # print(f'brc_x = {brc_x}')
    # print(f'brc_y = {brc_y}')
    # print(f'ball.rect.center = {ball.rect.center}')
    brick_collide_list = pygame.sprite.spritecollide(ball, brick_sprites_list, False)
    for brick in brick_collide_list:
        print(f"COLLISION WK BALL: {brick}")
        # print(f'brc_x[-2] = {brc_x[len(brc_x)-1]}')
        # print(f'BALL RECT TOP = {ball.rect.top}')
        # print(f'BRICK RECT BOTTOM = {brick.rect.bottom}')

        # ball is moving down+right
        if (brc_x[-2] - brc_x[-1]) < 0 and (brc_y[-2] - brc_y[-1]) < 0:
            print('down+right')
            if ball.rect.right in [i for i in range(brick.rect.left, brick.rect.left+collision_buffer)]:
                print('BALL HIT L')
                ball_motion[0] *= -1
            elif ball.rect.bottom in [i for i in range(brick.rect.top, brick.rect.top+collision_buffer)]:
                print('BALL HIT BOTTOM')
                ball_motion[1] *= -1
        # ball is moving down+left
        elif (brc_x[-2] - brc_x[-1]) > 0 and (brc_y[-2] - brc_y[-1]) < 0:
            print('down+left')
            if ball.rect.left in [i for i in range(brick.rect.right-collision_buffer, brick.rect.right)]:
                print('BALL HIT R')
                ball_motion[0] *= -1
            elif ball.rect.bottom in [i for i in range(brick.rect.top, brick.rect.top+collision_buffer)]:
                print('BALL HIT BOTTOM')
                ball_motion[1] *= -1
        # ball is moving up+right
        elif (brc_x[-2] - brc_x[-1]) < 0 and (brc_y[-2] - brc_y[-1]) > 0:
            print('up+right')
            if ball.rect.right in [i for i in range(brick.rect.left, brick.rect.left+collision_buffer)]:
                print('BALL HIT L')
                ball_motion[0] *= -1
            elif ball.rect.top in [i for i in range(brick.rect.bottom-collision_buffer, brick.rect.bottom)]:
                print('BALL HIT BOTTOM')
                ball_motion[1] *= -1
         # ball is moving up+left
        elif (brc_x[-2] - brc_x[-1]) > 0 and (brc_y[-2] - brc_y[-1]) > 0:
            print('up+left')
            if ball.rect.left in [i for i in range(brick.rect.right-collision_buffer, brick.rect.right)]:
                print('BALL HIT R')
                ball_motion[0] *= -1
            elif ball.rect.top in [i for i in range(brick.rect.bottom-collision_buffer, brick.rect.bottom)]:
                print('BALL HIT BOTTOM')
                ball_motion[1] *= -1
        else:
            print('WUT')

        all_sprites_list.remove(brick)
        brick_sprites_list.remove(brick)

    # print(ball.rect.bottom)
    # print(ball.rect.top)

    # Ball movement
    if ball.rect.right > SCREEN_WIDTH:
        ball_motion[0] *= -1
    elif ball.rect.left < 0:
        ball_motion[0] *= -1
    elif ball.rect.top < 0:
        ball_motion[1] *= -1
    # elif ball.rect.bottom > SCREEN_HEIGHT - 70:
    #     ball_motion[1] *= -1
    if ball.rect.colliderect(paddle.rect):
        # ball_motion[0] *= -1
        ball_motion[1] *= -1

    ball.rect.move_ip(ball_motion)

    brc_x.append(ball.rect.center[0])
    brc_y.append(ball.rect.center[1])
    brc_x.pop(0)
    brc_y.pop(0)

    all_sprites_list.update()

    # screen.fill('gray')
    screen.blit(bkg_img, bkg_rect)
    all_sprites_list.draw(screen)
    pygame.display.update()

    clock.tick(60)

pygame.quit()