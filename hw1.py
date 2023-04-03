import random
import pygame
from pygame.constants import QUIT

pygame.init()

screen = width, height = 800, 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255
COLORS = [(100, 100, 100), (220, 220, 220), (231, 123, 58), (45, 113, 24)]

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill(WHITE)
ball_rect = ball.get_rect()
ball_speed = [1, 1]

is_working = True
while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    ball_rect = ball_rect.move(ball_speed)
    if ball_rect.bottom >= height or ball_rect.top <= 0:
        ball_speed[1] = -ball_speed[1]
        ball.fill(COLORS[random.randint(0, 4)])

    if ball_rect.left >= width or ball_rect.right <= 0:
        ball_speed[0] = -ball_speed[0]
        ball.fill(COLORS[random.randint(0, 4)])

    main_surface.fill(BLACK)
    main_surface.blit(ball, ball_rect)
    pygame.display.flip()
