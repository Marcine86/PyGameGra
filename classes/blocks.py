import pygame
from classes.colors import BLOCK_COLORS
from classes.position import Position

class Block: # Klasa reprezentująca pojedynczy blok
    def __init__(self, id, cell_size=30):
        self.id = id
        self.cells = {}
        self.cell_size = cell_size
        self.rotation_state = 0
        self.row_offset = 0
        self.col_offset = 0

    def move(self, rows, cols):
        self.row_offset += rows
        self.col_offset += cols

    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0
    
    def unrotate(self):
        self.rotation_state -= 1
        if self.rotation_state < 0:
            self.rotation_state = len(self.cells) - 1

    def get_positioned_cells(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.x + self.col_offset, position.y + self.row_offset)
            moved_tiles.append(position)
        return moved_tiles
        
    def draw(self, screen):
        tiles = self.get_positioned_cells()
        for tile in tiles:
            x = tile.x * self.cell_size
            y = tile.y * self.cell_size
            tile_rect = pygame.Rect((x, y, self.cell_size-1, self.cell_size-1))
            pygame.draw.rect(screen, BLOCK_COLORS[self.id], tile_rect) # Rysowanie płytek bloku