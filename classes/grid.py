import pygame

class Grid:
    def __init__(self, rows=20, cols=10, cell_size=30):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.grid = [[0 for _ in range(self.cols)] for i in range(self.rows)]

    def is_inside(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def draw_grid(self, screen):
        for row in range(self.rows):
            for col in range(self.cols): # Rysowanie siatki do gry **AI**
                pygame.draw.rect(screen, (205,205,205), (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size), 1)