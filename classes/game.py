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
        self.game_over = False
        self.score = 0

    def update_score(self, rows_cleared): # Aktualizuje wynik na podstawie liczby usuniętych wierszy
        match rows_cleared:
            case 1:
                self.score += 100
            case 2:
                self.score += 300
            case 3:
                self.score += 500
        self.score += 10

    def get_random_block(self): # **AI** Bierze losowy blok z listy bloków
        """Get a random Tetris block"""
        block_class = random.choice(self.BLOCK_CLASSES)
        return block_class()
    
    def block_inside_grid(self): # Sprawdza czy blok jest w siatce
        tiles = self.current_block.get_positioned_cells()
        for tile in tiles:
            if not self.grid.is_inside(tile.y, tile.x):
                return False
        return True
    
    # Wygenerowane metody ruchu bloków **AI**
    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside_grid() or not self.block_fits():
            self.current_block.move(0, 1) # Cofnięcie ruchu w lewo, jeśli blok jest poza siatką
    
    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside_grid() or not self.block_fits():
            self.current_block.move(0, -1) # Cofnięcie ruchu w prawo, jeśli blok jest poza siatką

    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside_grid() or not self.block_fits():
            self.current_block.move(-1, 0) # Cofnięcie ruchu w dół, jeśli blok jest poza siatką
            self.lock_block()

    def rotate(self): # Obraca blok, a jeśli jest poza siatką, cofa obrót
        self.current_block.rotate()
        if not self.block_inside_grid():# Cofnięcie obrotu, jeśli blok jest poza siatką
            self.current_block.unrotate()

    def block_fits(self): # Sprawdza czy blok nie koliduje z innymi blokami
        tiles = self.current_block.get_positioned_cells()
        for tile in tiles:
            if not self.grid.is_empty(tile.y, tile.x):
                return False
        return True

    def lock_block(self): # Blokuje blok w siatce i generuje nowy blok
        tiles = self.current_block.get_positioned_cells()
        for tile in tiles:
            self.grid.grid[tile.y][tile.x] = self.current_block.id + 1  # Zablokowanie bloku w siatce
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        self.update_score(rows_cleared)
        if self.block_fits() == False:
            self.game_over = True

    def draw(self, screen): # Rysuję siatkę i bloki na ekranie
        self.grid.draw_grid(screen)
        self.current_block.draw(screen)
        self.next_block.draw(screen, 360, 250)