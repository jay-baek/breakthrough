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
    # PROBLEM: THE COLLISION IS ALWAYS DETECTED AS A TOP OR BOTTOM COLLISION.
    brick_collide_list = pygame.sprite.spritecollide(ball, brick_sprites_list, False)
    for brick in brick_collide_list:
        print(f"COLLISION WK BALL: {brick}")
        # print(f'BALL RECT TOP = {ball.rect.top}')
        # print(f'BRICK RECT BOTTOM = {brick.rect.bottom}')
        if ball.rect.right in [i for i in range(brick.rect.left, brick.rect.left+collision_buffer)]:
            # print('HIT R')
            ball_motion[0] *= -1
        elif ball.rect.left in [i for i in range(brick.rect.right-collision_buffer, brick.rect.right)]:
            # print('HIT L')
            ball_motion[0] *= -1
        elif ball.rect.top in [i for i in range(brick.rect.bottom-collision_buffer, brick.rect.bottom)]:
            # print('HIT TOP')
            ball_motion[1] *= -1
        elif ball.rect.bottom in [i for i in range(brick.rect.top, brick.rect.bottom+collision_buffer)]:
            # print('HIT BOTTOM')
            ball_motion[1] *= -1
        else:
            xy = random.choice([0, 1])
            ball_motion[xy] *= -1


        # if brick.rect.top <= ball.rect.bottom or brick.rect.bottom >= ball.rect.top:
        #     print('1')
        #     ball_motion[1] *= -1
        # elif brick.rect.right >= ball.rect.left or brick.rect.left <= ball.rect.right:
        #     print('2')
        #     ball_motion[0] *= -1
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

    all_sprites_list.update()

    # screen.fill('gray')
    screen.blit(bkg_img, bkg_rect)
    all_sprites_list.draw(screen)
    pygame.display.update()

    clock.tick(60)

pygame.quit()