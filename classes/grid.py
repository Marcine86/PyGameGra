import pygame

class Grid:
    def __init__(self, rows=20, cols=10, cell_size=30):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.grid = [[0 for _ in range(self.cols)] for i in range(self.rows)]

    def is_inside(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols
    
    def is_empty(self, row, col):
        return self.grid[row][col] == 0

    def draw_grid(self, screen):
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
                pygame.draw.rect(screen, (205, 205, 205), (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size), 1)