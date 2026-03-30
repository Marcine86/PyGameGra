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
    
    def draw(self, screen): # Rysuję siatkę i bloki na ekranie
        self.grid.draw_grid(screen)
        self.current_block.draw(screen)