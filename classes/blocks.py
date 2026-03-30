import pygame
from classes.colors import BLOCK_COLORS

class Block: # Klasa reprezentująca pojedynczy blok
    def __init__(self, id, cell_size=30):
        self.id = id
        self.cells = {}
        self.cell_size = cell_size
        self.rotation_state = 0
        
    def draw(self, screen): ### NIEUŻYTY ###
        tiles = self.cells[self.rotation_state]
        for tile in tiles:
            x = tile.x * self.cell_size
            y = tile.y * self.cell_size
            tile_rect = pygame.Rect((x, y, self.cell_size-1, self.cell_size-1))
            pygame.draw.rect(screen, BLOCK_COLORS[self.id], tile_rect) # Rysowanie płytek bloku