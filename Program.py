import pygame
import sys
from classes.game import Game
from classes.colors import (RED, GREEN, BLUE, YELLOW, CYAN, ORANGE)
WIDTH = 600
HEIGHT = 600

FPS = 60

BACKGROUND = (0,0,30)

# Inicjalizacja okna gry
pygame.init()

FONT = pygame.font.Font('ARCADE_N.TTF', 15)
SCORE = FONT.render('SCORE: ', True, (255, 255, 255))
NEXT_BLOCK = FONT.render('NEXT BLOCK: ', True, (255, 255, 255))

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
            if game.game_over:
                game.game_over = False
                game.__init__() # Restart gry
                game.current_block = game.get_random_block()
                game.next_block = game.get_random_block()
                game.score = 0
            if event.key == pygame.K_LEFT and not game.game_over:
                game.move_left() # Ruch w lewo
            if event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right() # Ruch w prawo
            if event.key == pygame.K_DOWN and not game.game_over:
                game.move_down() # Ruch w dół
            if event.key == pygame.K_SPACE and not game.game_over:
                game.rotate() # Obrót bloku
        if event.type == GAME_UPDATE and not game.game_over:
                game.move_down() # Automatyczny ruch w dół
    
    
    screen.fill(BACKGROUND)
    
    screen.blit(SCORE, (350, 50)) 
    
    SCORE_VALUE = FONT.render(str(game.score), True, (255, 255, 255))
    screen.blit(SCORE_VALUE, (450, 50))

    screen.blit(NEXT_BLOCK, (350, 200)) 
    
    if (game.game_over):
        GAME_OVER_TEXT = FONT.render("GAME OVER", True, RED)
        screen.blit(GAME_OVER_TEXT, (350, 400))
    
    game.draw(screen) # Rysuję grę na ekranie
    pygame.display.update()
    clock.tick(FPS)