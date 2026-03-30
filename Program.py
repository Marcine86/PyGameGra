import pygame
import sys
from classes.grid import Grid
from classes.tetris_blocks import create_block

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

block = create_block(0)
block.rotation_state = 0
block.move(1, 0)

while True: # Petla gry. Dzięki petli, gra będzie działać dopóki użytkownik jej nie zamknie
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill(BACKGROUND)
    game_grid.draw_grid(screen) # Rysowanie siatki do gry **AI**
    block.draw(screen)
    pygame.display.update()
    clock.tick(FPS)