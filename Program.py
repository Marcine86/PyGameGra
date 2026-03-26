import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

FPS = 60

BACKGROUND = (0,0,30)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ORION")
clock = pygame.time.Clock()

while True:
    screen.fill(BACKGROUND)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()