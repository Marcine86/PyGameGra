import pygame

class Grid:
    def __init__(self, rows=20, cols=10, cell_size=30):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.grid = [[0 for _ in range(self.cols)] for i in range(self.rows)]

    def is_inside(self, row, col): # Sprawdza pozycję wewnątrz siatki
        return 0 <= row < self.rows and 0 <= col < self.cols
    
    def is_empty(self, row, col): # Sprawdza czy podana komórka siatki jest pusta
        return self.grid[row][col] == 0

    def is_row_full(self, row): # Sprawdza czy dany wiersz jest pełny
        for cul in range(self.cols):
            if self.grid[row][cul] == 0:
                return False
        return True

    def clear_row(self, row): # Czyści dany wiersz
        for col in range(self.cols):
            self.grid[row][col] = 0

    def move_rows_down(self, row, num_rows): # Przesuwa ilość wierszy w dół
        for col in range(self.cols):
            self.grid[row+num_rows][col] = self.grid[row][col]
            self.grid[row][col] = 0

    def clear_full_rows(self): # Czyści pełne wiersze i przesuwa pozostałe w dół, zwraca liczbę usuniętych wierszy
        cleared = 0
        for row in range(self.rows-1, -1, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                cleared += 1
            elif cleared > 0:
                self.move_rows_down(row, cleared)
        return cleared

    def draw_grid(self, screen): # Rysuję siatkę i zablokowane bloki na ekranie
        from classes.colors import BLOCK_COLORS
        for row in range(self.rows):
            for col in range(self.cols):
                # Draw background
                pygame.draw.rect(screen, (20, 20, 50), (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))
                
                # Draw locked blocks
                if self.grid[row][col] != 0:
                    color = BLOCK_COLORS[self.grid[row][col] - 1]  # -1 because grid values are id + 1
                    pygame.draw.rect(screen, color, (col * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))
                
                # Draw grid lines
                #pygame.draw.rect(screen, (205, 205, 205), (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size), 1)