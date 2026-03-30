import pygame
import sys
from classes.game import Game
WIDTH = 600
HEIGHT = 600

FPS = 60

BACKGROUND = (0,0,30)

# Inicjalizacja okna gry
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TETRIS")
clock = pygame.time.Clock()

game = Game() # Instancja gry.

TIME = 300
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, TIME) # Ustawia timer, który co {TIME} milisekund wywołuje zdarzenie GAME_UPDATE

while True: # Petla gry. Dzięki petli, gra będzie działać dopóki użytkownik jej nie zamknie
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left() # Ruch w lewo
            if event.key == pygame.K_RIGHT:
                game.move_right() # Ruch w prawo
            if event.key == pygame.K_DOWN:
                game.move_down() # Ruch w dół
            if event.key == pygame.K_SPACE:
                game.rotate() # Obrót bloku
        if event.type == GAME_UPDATE:
                game.move_down() # Automatyczny ruch w dół
    screen.fill(BACKGROUND)
    game.draw(screen) # Rysuję grę na ekranie
    pygame.display.update()
    clock.tick(FPS)