import pygame, sys
from classes.colors import YELLOW, CYAN

def show_menu(screen, width): # Funkcja wyświetlająca menu startowe
    screen.fill((0, 0, 30))

    font_title = pygame.font.Font('ARCADE_N.TTF', 50)
    font_regular = pygame.font.Font('ARCADE_N.TTF', 15)
    font_heading = pygame.font.Font('ARCADE_N.TTF', 25)

    title = font_title.render("TETRIS", True, YELLOW)
    instruction1 = font_regular.render("< V > - move block left/down/right", True, CYAN)
    instruction2 = font_regular.render("Space - rotate block", True, CYAN)
    instruction3 = font_regular.render("P - save screenshot on game over", True, CYAN)
    play = font_heading.render("Press any key to start", True, YELLOW)
    
    screen.blit(title, (width//2 - title.get_width()//2, 150))
    screen.blit(instruction1, (width//2 - instruction1.get_width()//2, 250))
    screen.blit(instruction2, (width//2 - instruction2.get_width()//2, 280))
    screen.blit(instruction3, (width//2 - instruction3.get_width()//2, 310))
    screen.blit(play, (width//2 - play.get_width()//2, 360))

    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return