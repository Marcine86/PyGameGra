import pygame
import sys
from grid import Grid

WIDTH = 800
HEIGHT = 600

FPS = 60

BACKGROUND = (0,0,30)

# Inicjalizacja okna gry
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TETRIS")
clock = pygame.time.Clock()

game_grid = Grid()

while True: # Petlą gry
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill(BACKGROUND)
    game_grid.draw_grid(screen) # Rysowanie siatki do gry **AI**
    pygame.display.update()
    clock.tick(FPS)