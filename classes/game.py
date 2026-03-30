import random
from classes.grid import Grid
from classes.tetris_blocks import (
    I_Block, O_Block, T_Block, S_Block, Z_Block, J_Block, L_Block
)

class Game: # Interfejs do gry, zarządza logiką gry, blokami i siatką.
    BLOCK_CLASSES = [I_Block, O_Block, T_Block, S_Block, Z_Block, J_Block, L_Block]

    def __init__(self):
        self.grid = Grid()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def get_random_block(self): # **AI** Bierze losowy blok z listy bloków
        """Get a random Tetris block"""
        block_class = random.choice(self.BLOCK_CLASSES)
        return block_class()
    
    def block_inside_grid(self, block): # Sprawdza czy blok jest w siatce
        tiles = self.current_block.get_positioned_cells()
        for tile in tiles:
            if not self.grid.is_inside(tile.y, tile.x):
                return False
        return True
    
    # Wygenerowane metody ruchu bloków **AI**
    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside_grid(self.current_block):
            self.current_block.move(0, 1) # Cofnięcie ruchu w lewo, jeśli blok jest poza siatką
    
    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside_grid(self.current_block):
            self.current_block.move(0, -1) # Cofnięcie ruchu w prawo, jeśli blok jest poza siatką

    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside_grid(self.current_block):
            self.current_block.move(-1, 0) # Cofnięcie ruchu w dół, jeśli blok jest poza siatką

    def draw(self, screen): # Rysuję siatkę i bloki na ekranie
        self.grid.draw_grid(screen)
        self.current_block.draw(screen)